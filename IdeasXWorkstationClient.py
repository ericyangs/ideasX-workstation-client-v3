'''
Title: IdeasXWorkstationClient Class 
Author: Tyler Berezowsky 
Description: 
'''
import sys
import os
import getopt

try:
    import paho.mqtt.client as mqtt
    import paho.mqtt.publish as mqtt_pub
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

try:     
    from protocolbuffers import IdeasXMessages_pb2 as IdeasXMessages
    import IdeasXDatabaseManager 
except ImportError: 
    print("The python classes for IdeasX are missing. Try running the Makefile in" +
            "ideasX-messages.")
            
data = []

#------------------------------------------------------------------------------
# Sniffer Client Class

class IdeasXWorkstationClient(): 
    def __init__(self):
        self.command_topic = "/encoder/+/command"
        self.data_topic = "/encoder/+/data"
        self.health_topic = "/encoder/+/health"
        self.mqttdebug = False 
        self.debug = False
        
        self.dmb = IdeasXDatabaseManager.IdeasXDatabaseManager()
        
        self._mqttc = mqtt.Client(clean_session=True, userdata=None,
                protocol='MQTTv311')
        
        self._mqttc.message_callback_add(self.health_topic, self.mqtt_on_health)
        #self._mqttc.message_callback_add(self.data_topic, self.mqtt_on_data)
        #self._mqttc.message_callback_add(self.command_topic, self.mqtt_on_command)       
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_disconnect = self.mqtt_on_disconnect 
        
        if self.mqttdebug: 
            self._mqttc.on_log = self.mqtt_on_log 

#------------------------------------------------------------------------------
# callback functions

    def mqtt_on_connect(self, mqttc, backend_data, flags, rc): 
        if rc == 0: 
            print('Connected to %s: %s' % (mqttc._host, mqttc._port))
        else: 
            print('rc: ' + str(rc))
        print('-'*70)

    def mqtt_on_disconnect(self, mqttc, backend_data, rc):
        if self.debug: 
            if rc != 0: 
                print("Client disconnected and its a mystery why!")
            else: 
                print("Client successfully disconnected.") 
            self.print_line()            

    def mqtt_on_health(self, mqttc, backend_data, msg):
        '''
        try: 
            self.dmb.parseHealthMessage(msg.payload)
        except: 
            print("Error: Failure to parse message")
            if self.debug:
                print("Raw Message: %s\n" %msg.payload)
        '''
        self.dmb.parseHealthMessage(msg.payload)
        self.print_line()
        

    def mqtt_on_log(self, mqttc, backend_data, level, string):
        print(string)
        self.print_line()


#------------------------------------------------------------------------------
# General API Calls 
        
    def startWorkstationClient(self, ip="server.ideasX.tech", port=1883, keepalive=60):     
        self.ip = ip 
        self.port = port 
        self.keepalive = keepalive 
        self._mqttc.connect(ip, port, keepalive)      # connect to broker
        #self._mqttc.subscribe(self.command_topic, 2)
        self._mqttc.subscribe(self.health_topic, 1)
        #self._mqttc.subscribe(self.data_topic, 2)                              
        self._mqttc.loop_forever() # need to use blocking loop otherwise python will kill process
    
            
    def print_line(self):
        print('-'*70)
        

    
if __name__ == "__main__": 
    argv = sys.argv[1:] 
    wsc = IdeasXWorkstationClient()
    Host = "ideasx.duckdns.org"
    Port = 1883 
    KeepAlive = 30
    msgFlag = False;     
    deviceID = None; 
    cmdPayload = None; 
    cmdArg = None;
    
    try: 
        opts, args = getopt.getopt(argv, "d:h:k:p:t:c:o:",
                                  ['device-id','host', 'keepalive',
                                  'port', 'topic(s)','command', 'payload'])
    except getopt.GetoptError as s: 
        sys.exit(2)
    for opt, arg in opts: 
        if opt in ("-h", "--host", "--hostname"):
            Host = arg
        elif opt in ("-d", "--device-id"):
            deviceID = arg
        elif opt in ("-k", "--keepalive"):
            KeepAlive = arg 
        elif opt in ("-p", "--port"):
            Port = arg
        elif opt in ("-o", "--payload"):
            cmdPayload = arg.encode('utf-8')
        elif opt in ("-c", "--command"):
            msgFlag = True
            cmdArg = arg
   
            
    if msgFlag:
        if cmdArg in IdeasXMessages._COMMANDMESSAGE_COMMAND.values_by_name.keys():
            msg = IdeasXMessages.CommandMessage(); 
            msg.command = IdeasXMessages.CommandMessage.Command.Value(cmdArg)
            if cmdPayload != None:
                msg.payload = cmdPayload
            if deviceID != None:
                pubTopic = "/modules/"+deviceID+"/command"
            else:
                sys.exit(2)
#            sc.print_line()                
#            print("Preparing Message...")
#            sc.print_line()
#            print("Device ID: "+str(deviceID))            
#            sc.print_line()            
#            print(msg.__str__()[:-1])
         
            mqtt_pub.single(topic=pubTopic,
                        payload=msg.SerializeToString().decode('utf-8'),
                        retain = False, 
                        qos=2,
                        hostname=Host,
                        port=Port)
            wsc.print_line()
            print("Message Sent")
            wsc.print_line()
            sys.exit(0)
        else:
            sys.exit(2)
    else:
        wsc.startWorkstationClient(ip = Host, port = Port, keepalive = KeepAlive)
     
