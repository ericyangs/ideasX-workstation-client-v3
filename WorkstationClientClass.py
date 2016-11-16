'''
Title: IdeasXDatabaseManager Class
Author: Tyler Berezowsky 
Description: 

This class requires the following functionality: 

1) Connect to the IdeasX system (MQTT Client) 
    - Connect using the devices MAC Address as the Client ID 
    - Autoreconnect if the device failts 
    - The abililty to start a broker in a seperate thread if no broker is available 
    - The ability to store settings in a SQLite File or setting .txt file. 
2) The ability to induce a system wide keypress in the following systems: 
    - Windows 
    - Mac 
    - Linux
3) Create a table in memory of the IdeasX devices currently in the system
4) Parse IdeasX messages types given nothing more than a protofile 
5) Subscribe to IdeasX devices 
6) Invoke keystrokes if proper messages in a command is sent. 
'''
import sys
import time
import collections
from ParsingToolsClass import ParsingTools

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
except ImportError: 
    print("The python classes for IdeasX are missing. Try running the Makefile in" +
            "ideasX-messages.")
    
class WorkstationClientClass(): 
    def __init__(self, settingFile=None, clientID = None, debug=True, mqttdebug=True):
        # Private Class Flags and Variables
        self.__clientID = clientID
        self.__settingFile = settingFile
        self.__debug = debug 
        self.__mqttDebug = mqttdebug 
        self.__errorIndex = 0 
        self.__refreshCb = None
        
        
        # MQTT Topics 
        self.__DEVICETYPE = ["/encoder/+"]
        self.__COMMANDTOPIC = "/command"
        self.__DATATOPIC = "/data"
        self.__HEALTHTOPIC = "/health"
                
        # Data Structure for Encoders / Actuators 
        self.encoders = {}
        self.subscribedEncoders = []
        
        # IdeasX Parsers
        self._healthParser = IdeasXMessages.HealthMessage()
        self._dataParser = IdeasXMessages.DataMessage()
        self._commandParser = IdeasXMessages.CommandMessage()
        self._parserTools = ParsingTools()

        # MQTT Client Object
        self._mqttc = mqtt.Client(self.__clientID, clean_session=True, userdata=None, protocol='MQTTv311')
        
        # Setup Callback Functions for each device type
        for device in self.__DEVICETYPE:
            self._mqttc.message_callback_add(device+self.__HEALTHTOPIC, self.mqtt_on_health)
            self._mqttc.message_callback_add(device+self.__DATATOPIC, self.mqtt_on_data)
            #self._mqttc.message_callback_add(device+self.__COMMANDTOPIC, self.mqtt_on_command)       
        
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_disconnect = self.mqtt_on_disconnect 
        #self._mqttc.on_subscribe = self.mqtt_on_subscribe 
        #self._mqttc.on_unsubscribe = self.mqtt_on_unsubscribe
        
        if self.__mqttDebug: 
            self._mqttc.on_log = self.mqtt_on_log 

#------------------------------------------------------------------------------
# callback functions

    def mqtt_on_connect(self, mqttc, backend_data, flags, rc): 
        if rc == 0: 
            self.printInfo('Connected to %s: %s' % (mqttc._host, mqttc._port))
        else: 
            self.printInfo('rc: ' + str(rc))
        self.printLine()

    def mqtt_on_disconnect(self, mqttc, backend_data, rc):
        if self.__debug: 
            if rc != 0: 
                self.printError("Client disconnected and its a mystery why!")
            else: 
                self.printInfo("Client successfully disconnected.") 
            self.printLine()   
            
    def mqtt_on_log(self, mqttc, backend_data, level, string):
        print(string)
        self.printLine()         
                        
    def mqtt_on_data(self, mqttc, backend_data, msg):
        self.printInfo("Data Message")
        self.printLine()
        try: 
            self._dataParser.ParseFromString(msg.payload)
            print("GPIO States: " + bin(self._dataParser.button))
        except: 
            self.printError("Failure to parse message")
            if self.__debug:
                print("Raw Message: %s" %msg.payload)
            self.printLine()
            
    def mqtt_on_health(self, mqttc, backend_data, msg):
        self.printInfo("Health Message")
        self.printLine()
        try: 
            self._healthParser.ParseFromString(msg.payload)
            macID = self._parserTools.macToString(self._healthParser.module_id)
            
            if self._healthParser.alive:
                temp_list = []
                for field in self._healthParser.ListFields():
                    temp_list.append((field[0].name, field[1]))  
                temp_list.append(('time', time.time()))          
                self.encoders[macID] = collections.OrderedDict(temp_list)
            else:
                try: 
                    self.encoders.pop(macID)
                except KeyError: 
                    self.printError("Encoder ID " +macID+" is not stored")
            
            if self.__refreshCb: 
                print("FUUUUUUUUUUUUUUUUUCK")
                self.__refreshCb()
            
            if self.__debug:
                for encoder, fields in zip(self.encoders.keys(), self.encoders.values()): 
                    print(str(encoder) +" : "+ str(fields))
                self.printLine()
        except: 
            self.printError("Error: Failure to parse message")
            if self.__debug:
                print("Raw Message: %s" %msg.payload)
            self.printLine()
        


        

#----------------------------------------------thy--------------------------------
# General API Calls 
        
    def cmdStartWorkstationClient(self, ip="server.ideasX.tech", port=1883, keepAlive=60):     
        self.ip = ip 
        self.port = port 
        self.keepAlive = keepAlive 
        
        self.printLine()
        self.printInfo("Starting Workstation Client (WSC)")
        self.printLine()
        
        try:  
            self._mqttc.connect(self.ip, self.port, self.keepAlive)      # connect to broker
            
            for device in self.__DEVICETYPE:
                self._mqttc.subscribe(device + self.__HEALTHTOPIC, 1)
            self._mqttc.loop_forever() # need to use blocking loop otherwise python will kill process
        except:
            self.printError("There was a fucking mistake here.")
            sys.exit(1)
            
    def guiStartWorkstationClient(self, ip="server.ideasx.tech", port=1883, keepAlive=60):
        self.ip = ip 
        self.port = port 
        self.keepAlive = keepAlive
        
        self.printLine()
        self.printInfo("Starting Workstation Client (WSC)")
        self.printLine()
        
        try: 
            self._mqttc.connect(self.ip, self.port, self.keepAlive)
            for device in self.__DEVICETYPE:
                self._mqttc.subscribe(device + self.__HEALTHTOPIC, 0)
                self._mqttc.subscribe(device + self.__DATATOPIC, 0)
            self._mqttc.loop_start() # start MQTT Client Thread 
        except: 
            self.printError("There was a fucking mistake here.")
            sys.exit(1)
            
            
    def restartWSC(self):
        self.printInfo("This really doesn't do anything")
    
    def killWSC(self):
        self._mqttc.loop_stop()
        self.printInfo("Murdered MQTT thread.")
        
    def attachRefreshCallback(self, cb):
        self.__refreshCb = cb
        
            
    def activateEncoder(self, deviceMACAddress, deviceType=None):
        '''
        Subscribe to device's data topic and send activate command if device 
        is not active. 
        
        * Currently does not confirm subscribe is successful 
        * Currently does not send the activate command as it does not exist
        
        deviceType = str 
        deviceMACAddress = str(MAC_ID)
        '''
        if deviceMACAddress in self.encoders.keys():
            if deviceType == None: 
                deviceDataTopic = self.__DEVICETYPE[0] + deviceMACAddress + self.__DATATOPIC
            else: 
                deviceDataTopic = deviceType + deviceMACAddress + self.__DATATOPIC
                 
            self._mqttc.subscribe(deviceDataTopic, 1)
            self.subscribedEncoders.append(deviceMACAddress)
            if self.__debug: 
                self.printInfo("Device " + deviceMACAddress + " data topic was subscribed")
        else: 
            self.printError("Device " + deviceMACAddress + " is not currently in the IdeasX system.")
            
    def deactivateEncoder(self, deviceMACAddress, deviceType=None, forceAction=False):
        '''
        Unsubscribe from device's data topic and send deactive command if no other WSC are using device. 
        
        * Currently does not confirm unsubscribe is successful 
        * Currently does not send the deactive command as it does not exist and I don't know how to sync that shit. 
        '''
        if (deviceMACAddress in self.encoders.keys()) or (forceAction): 
            if deviceType == None: 
                deviceDataTopic = self.__DEVICETYPE[0] + deviceMACAddress + self.__DATATOPIC
            else: 
                deviceDataTopic = deviceType + deviceMACAddress + self.__DATATOPIC 
            self._mqttc.unsubscribe(deviceDataTopic)
            self.subscribedEncoders.remove(deviceMACAddress)
            if self.__debug: 
                self.printInfo("Device " + deviceMACAddress + " data topic was unsubscribed")
        else: 
            self.printError("Device " + deviceMACAddress + " is not currently in the IdeasX System")    


    def shutdownDevice(self, deviceMACAddress, deviceType=None):
        self._commandParser.command = self._commandParser.SHUT_DOWN
        self._mqttc.publish(self.__DEVICETYPE[0][:-1] + deviceMACAddress + self.__COMMANDTOPIC,
                            self._commandParser.SerializeToString().decode('utf-8') ,
                            qos=1,
                            retain=False)
        self.printInfo("Send Shutdown Command to Encoder " + deviceMACAddress)
        
    def printLine(self):
        print('-'*70)
        
    def printError(self, errorStr):
        self.__errorIndex = self.__errorIndex + 1
        print("WSC Error #" + str(self.__errorIndex) + ": " + errorStr)
    
    def printInfo(self, msgStr):
        print("WSC: " + msgStr)
        

if __name__ == "__main__": 
    Host = "ideasx.duckdns.org"
    Host = "192.168.0.101"
    Host = "10.42.0.1"
    Port = 1883 
    KeepAlive = 30
    msgFlag = False;     
    deviceID = None; 
    cmdPayload = None; 
    cmdArg = None;
    cmdTest = False; 
    
    
    wsc = WorkstationClientClass()
    
    if cmdTest: 
        wsc.cmdStartWorkstationClient(Host, Port, KeepAlive)
    else: 
        wsc.guiStartWorkstationClient(Host, Port, KeepAlive)
        time.sleep(3)
        wsc.activateEncoder('18:fe:34:f1:f2:8d')
        print(wsc.subscribedEncoders)
        time.sleep(2)
        wsc.deactivateEncoder('18:fe:34:f1:f2:8d')
        print(wsc.subscribedEncoders)
        time.sleep(10)
        wsc.killWSC()
        