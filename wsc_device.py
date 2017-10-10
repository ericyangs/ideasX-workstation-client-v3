import time
from wsc_tools import ParsingTools
from wsc_tools import Switch
from wsc_device_encoder import Encoder

class DeviceManager():
    FAIL = 0 
    SUCCESS = 1
    
    def __init__(self, deviceClass, mqttc, healthSignal=None):
        self.__healthSignal = healthSignal
        self.__devices = {} 
        self.__deviceClass = deviceClass
        self.__parserTools = ParsingTools()
        self.__mqttc = mqttc 


    def setupMQTT(self):
        self.__mqttc.subscribe(self.__deviceClass.DEVICE_HEALTH_TOPIC,
                               self.__deviceClass.DEVICE_HEALTH_QOS)

        self.__mqttc.message_callback_add(self.__deviceClass.DEVICE_HEALTH_TOPIC, 
                                          self.mqtt_health_cb)

    def mqtt_health_cb(self, mqttc, backend_data, msg): 
        macID = self.__parserTools.getIDfromTopic(msg.topic)
        field = self.__parserTools.getFieldfromTopic(msg.topic)
        r = self.updateDevice(macID, field, msg.payload)
        if (r == DeviceManager.FAIL): 
            self.addDevice(macID, mqttc)
            self.updateDevice(macID, field, msg.payload)
        if (self.__healthSignal):
            self.__healthSignal.emit(self.listAliveDevices())        
        
    def updateDevice(self, device_id, field, payload):
        if device_id in self.__devices.keys(): 
            if (self.__devices[device_id].updateField(field, payload) == self.__deviceClass.SUCCESS):
                return DeviceManager.SUCCESS 
        else: 
            return DeviceManager.FAIL 
    
    def listAliveDevices(self): 
        tempDict = {}
        for device in self.__devices.keys(): 
            e = self.__devices[device]
            if (e.getField(self.__deviceClass.ALIVE_TOPIC) == self.__deviceClass.ALIVE_VALUE):
                tempDict[device] = e
        return tempDict
    
    def listDevices(self):
        return self.__devices.keys()
    
    def addDevice(self, device_id, mqttc): 
        self.__devices[device_id] = self.__deviceClass(device_id, mqttc)
        
    def removeDevice(self, device_id):
        if device_id in self.__devices.keys():
            self.__devices.pop(device_id)
            return DeviceManager.SUCCESS
        else: 
            return DeviceManager.FAIL
        
    def getDevice(self, device_id): 
        if device_id in self.__devices.keys(): 
            return self.__devices[device_id]
        else: 
            return DeviceManager.FAIL
        
            
if __name__ == "__main__": 
    device_id0 = "12:23:32:32:32:32"
    device_id1 = "12:23:32:32:31:32"

    dm = DeviceManager(Encoder, None)
    print("Updating Nonexistanct Device Result" + str(dm.updateDevice(device_id0, 'ota', b'1')))
    print("Adding device:" + str(dm.addDevice(device_id0)))
    print("Adding device:" + str(dm.addDevice(device_id1)))

    print("Updating Device Result" + str(dm.updateDevice(device_id0, 'ota', '1')))
    print("Updating Device Result" + str(dm.updateDevice(device_id1, 'alive', '1')))
    
    print(dm.listAliveDevices())

