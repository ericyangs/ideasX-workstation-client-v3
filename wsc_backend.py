#!/usr/bin/python

'''
 
WORKSTATION CLIENT BACKEND

'''


import sys
try:
    import paho.mqtt.client as mqtt
except ImportError:
    # This part is only required to run the example from within the examples
    # directory when the module itself is not installed.
    #
    # If you have the module installed, just use "import paho.mqtt.client"
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.client as mqtt
# NOTE: This needs to be replaced with a QT, TKinker alternative. 
# from wx.lib.pubsub import pub
from packet_handling import decode_client_list, decode_data_packet
try: 
    from ctype_bindings import SwitchPro6
    windows = True
except AttributeError: 
    print("Windows win32 API missing.\n Button presses will be still be represented in print statements.") 
    global print_debug 
    windows = False

#------------------------------------------------------------------------------
# WORKSTATIONCLIENT CLASS

class WorkstationClientClass():
    def __init__(self, client_id=None, debug=True, mqttdebug=False):
        self.client_id = client_id 
        self.debug = debug
        self.mqttdebug = mqttdebug
        self.mode_color = 'debug'
            
        self.data_topics = '/modules/+/data'
        self.clientlist_topic = '/workstations/modulehealth'
        self.clientlist = None 
        self.subscribed_modules = []
        if windows:
            self.switchpro6 = SwitchPro6()
        self._mqttc = mqtt.Client(self.client_id, clean_session=True, userdata=None, 
                        protocol='MQTTv311')
        self._mqttc.message_callback_add(self.clientlist_topic, self.mqtt_on_client_list) 
        self._mqttc.message_callback_add(self.data_topics, self.mqtt_on_data)
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_disconnect = self.mqtt_on_disconnect        
        if self.mqttdebug: 
            self._mqttc.on_log = self.mqtt_on_log
            
#------------------------------------------------------------------------------
# callback functions

    def mqtt_on_connect(self, mqttc, backend_data, flags, rc):
        # pub.sendMessage('status.connection', status = [mqttc._host, mqttc._port, rc])
        if self.debug: 
            if rc == 0: 
                print('Connected to %s: %s' % (mqttc._host, mqttc._port))
            else: 
                print('rc: ' + str(rc))

    def mqtt_on_client_list(self, mqttc, backend_data, msg):
        self.clientlist = decode_client_list(msg.payload) 
        
        for active_module_id in self.subscribed_modules: 
            for dead_module_id in self.clientlist[self.clientlist['alive']==0]['module_id']: 
                if active_module_id == dead_module_id: 
                    if self.debug: 
                        print("Conflicting ID: " + str(active_module_id)+ \
                        "\nAttempting to kill now.")
                    self.unsubscribe_to_module(active_module_id)
        if self.debug: 
            print(self.clientlist)
        # pub.sendMessage('data.clientlist', data = self.clientlist)
       
        
    def mqtt_on_data(self, mqttc, backend_data, msg):
        #pub.sendMessage('data.module', data=msg.payload)
        data =  decode_data_packet(msg.payload)
        if windows:     
            self.switchpro6.keymap_press(data[0])
        if self.debug: 
            print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload)+" "+str(data))

    def mqtt_on_log(self, mqttc, backend_data, level, string):
        print(string)
    
    def mqtt_on_disconnect(self, mqttc, backend_data, rc):
        # pub.sendMessage('status.connection', status = [None, None, rc])
        if self.debug: 
            if rc != 0: 
                print("Client disconnected and its a mystery why!")
            else: 
                print("Client successfully disconnected.") 
#------------------------------------------------------------------------------
# General API Calls 
        
    def start_workstation_client(self, ip="127.0.0.1", port=1883, keepalive=60):     
        self.ip = ip 
        self.port = port 
        self.keepalive = keepalive 
        self.clientlist = None
        self._mqttc.connect(ip, port, keepalive)      # connect to broker                              
        self._mqttc.subscribe(self.clientlist_topic, 2)    # subscribe to client list 
        self._mqttc.loop_start() # Start a thread handling network traffic   
    
    def subscribe_to_module(self, module_id): 
        module_found = False
        if type(module_id) == int: 
            module_id = str(module_id) 
        if len(module_id) < 8:
            module_id = '0'*(8-len(module_id)) + module_id
	
        for active_module_id in self.clientlist[self.clientlist['alive']==1]['module_id']:
            if int(module_id) == active_module_id: 
                module_found = True
                module_topic = '/modules/'+module_id+'/data'
                result, mid =  self._mqttc.subscribe(module_topic, qos=0)
                # pub.sendMessage('status.subscribe', status=[int(module_id), result, mid])
                if result == 0:
                    if int(module_id) not in self.subscribed_modules: 
                        self.subscribed_modules.append(int(module_id))
                        #pub.sendMessage('data.subscribed_modules', data=self.subscribed_modules)
                        if self.debug: 
                            print("Module %s was successfully added" % module_id)
                    else: 
                        if self.debug: 
                            print("Module is already subscribed")
                return result, mid
        if module_found == False:
            if self.debug: 
                print("Module is not alive or in client list.") 
                print("Module ID: " + str(module_id))
                return 3, None 
        
    def unsubscribe_to_module(self, module_id): 
        if type(module_id) == int: 
            module_id = str(module_id) 
        if len(module_id) < 8:
            module_id = '0'*(8-len(module_id)) + module_id
        
        if int(module_id) in self.subscribed_modules: 
            module_topic = '/modules/'+module_id+'/data'
            result, mid = self._mqttc.unsubscribe(module_topic)
            # pub.sendMessage('status.unsubscribe', status=[int(module_id), result, mid])
            if result == 0: 
                self.subscribed_modules.remove(int(module_id))
                #pub.sendMessage('data.subscribed_modules', data=self.subscribed_modules)    # send all the subs
                if self.debug: 
                    print("Module %s was successfully removed" % module_id)
            return result, mid            
        else:            
            if self.debug: 
                print("Module is not subscribed") 
                print("Subscribed Modules:\n", self.subscribed_modules)
            return 3, None 

#-----------------------------------------------------------------------------
# Puck Connectivity 	
# The Puck will function under the following methods. 
# 1. The puck will make the system aware of it's presence through a health 
#    message to the database client. There needs to be sometype of addition
#    flag or delimiter for the database client to know it is a puck. 
# 2. The backend needs to forward this flag via pubsub. 
# 3. There needs to be function to pair a module to a puck with the following
#    house keeping skills: 
#    a. Automatically unpairs if module or puck dies 
#    b. will not pair if puck or module is already connected to computer or 
#       paired with another computer. 
#    c. sends a message to puck to listen to the topic of a specific module. 
#    d. confirms puck is listening through sometype of verification QoS = 2? 
# 

    def pair_module_to_puck(self, module_id, puck_id, pair=True):
        if type(module_id) == int: 
            module_id = str(module_id)
        if len(module_id)<8: 
            module_id = '0'*(8-len(module_id)) + module_id         
        if type(puck_id) == int: 
            puck_id = str(puck_id)
        if len(puck_id)<8: 
            puck_id = '0'*(8-len(puck_id)) + puck_id 
        
        module_found = False
        # update to insure puck is alive
        # modifiy so pandas only is loooking at modules
        for active_module_id in self.clientlist[self.clientlist['alive']==1]['module_id']:
            if int(module_id) == active_module_id :
                module_found = True 
                puck_topic = '/pucks/'+puck_id+'/command'
                if pair:
                    payload = 'a/modules/'+str(module_id)+'/data'
                else: 
                    payload = 'd/modules/'+str(module_id)+'/data'
                result, mid =  self._mqttc.publish(puck_topic, payload, 0, retain=False)
                if result == 0: 
                    # self.subscribed_modules.remove(int(module_id))
                    # pub.sendMessage('data.paired_modules', data=self.subscribed_modules)    # send all the subs
                    if self.debug: 
                        print("Module %s was successfully paired" % module_id)
                    return result, mid    

        if module_found == False:
            if self.debug: 
                print("Module is not alive or in client list.")
                print("Module ID: " + str(module_id))
                return 3, None 
        
        
                
if __name__ == "__main__": 
    wsc = WorkstationClientClass() 
    wsc.start_workstation_client(ip="server.ideasx.tech")
