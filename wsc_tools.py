import  pyautogui as ue
import serial 
import serial.tools.list_ports
import logging
import time

class EncoderConfig():
    BAUD_RATE = 115200
    SET_AP_COMMAND = "AT+WA="
    CLEAR_APS_COMMAND = "AT+WC=" 
    LIST_APS_COMMAND = "AT+WL"
    
    def __init__(self):
        self.__ports = None
        self.__ser = None
        self.__port = None

    def setPort(self, port):        
        if self.__ser != None:
            self.__ser.close() 
        self.__port = port

    def close(self):
        if self.__ser != None:
          self.__ser.close()

    def connect(self, port=None):
        if port != None: 
            self.port = port 
        self.__ser = serial.Serial(port = self.port, baudrate=EncoderConfig.BAUD_RATE, timeout=3)
        #self.__ser.open()

    def reset(self): 
        self.__ser.setDTR(value=1) 
        time.sleep(0.5)
        self.__ser.setDTR(value=0)
        time.sleep(0.5)

    def getPort(self): 
        return self.__port

    def getPorts(self):
        temp = []
        self.__ports = serial.tools.list_ports.comports()
        for port in self.__ports: 
            temp.append(port[0])
        return temp    

    def clearWifiAPs(self, port): 
        self.connect(port)
        clear_str = "\n\r"
        clear_str = clear_str.encode('utf-8')
        self.__ser.write(clear_str)
        
    
    def setWifiAPs(self, aps, port): 
        self.connect(port)
        clear_str = "\n\r"
        clear_str = clear_str.encode('utf-8')
        time.sleep(0.5)
        self.__ser.write(clear_str)
        time.sleep(0.5)
        factory_reset_str = "\n\rAT+FRST\n\r"
        factory_reset_str = factory_reset_str.encode('utf-8')
        self.__ser.write(factory_reset_str)
        time.sleep(0.5)
        for creds in aps: 
            self.setWifiAP(creds[0], creds[1])
            time.sleep(1)

        self.__ser.write(clear_str)
        time.sleep(0.5)
        ## do hard reset 
        self.reset()
        
        ##reset_str = "\n\rAT+RST\r\n"
        ##reset_str = reset_str.encode('utf-8')
        ##self.__ser.write(reset_str)
        
        self.__ser.close()

    def setWifiAP(self, ssid, password=None):
        if not self.__ser.isOpen():
            return 
    
        command_str = EncoderConfig.SET_AP_COMMAND + ssid + "," + password + "\r\n"
        command_str = command_str.encode('utf-8')
        self.__ser.write(command_str)        

    def clearWifiAPs(self, port):
        pass

    def getWifiConfig(self): 
        pass

    def setBrokerConfig(self):
        pass

    def getBrokerConifg(self): 
        pass

class ParsingTools():
    def macToString(self, mac_bytes):
        ''' Convert uint8 byte string to "XX:XX:XX:XX:XX"
        '''
        mac_str = ""
        for byte in mac_bytes:
            mac_str = mac_str + format(byte, '02x') + ':'
        return mac_str[:-1].format('utf-8')

    def calculateVCell(self, raw_Vcell):
        raw_Vcell = int(raw_Vcell.decode('utf-8'))
        return raw_Vcell*1.25e-3

    def calculateSOC(self, raw_SOC):
        raw_SOC = int(raw_SOC.decode('utf-8'))
        soc = raw_SOC.to_bytes(2, 'big')[0]
        if (soc > 100):
            return 100
        else: 
            return raw_SOC.to_bytes(2, 'big')[0]

    def getIDfromTopic(self, topic):
        return topic.split('/')[1]
    
    def getFieldfromTopic(self, topic): 
        return topic.split('/')[3]

    def getStr(self, byteCode): 
        return byteCode.decode('utf-8')

class FieldGenerator():
    def generateMACID(self):
        import numpy as np
        macID = np.random.randint(255, size=5)
        macStr = ""
        for val in macID:
            macStr = macStr + format(val, 'x') + ":"
        return macStr[:-1]

    def generateRSSI(self):
        import numpy as np
        rssi = np.random.randint(80)
        rssiStr = "RSSI:  -" + str(rssi) + "dBm"
        return rssiStr

    def generateSOC(self):
        import numpy as np
        soc = np.random.randint(100)
        socStr = "Battery:  " + str(soc) + "%"
        return socStr

    def generateStatus(self):
        import numpy as np
        hr = np.random.randint(12) + 1
        min = np.random.randint(60)
        ampm = np.random.randint(1)
        statusStr = "Last Update: " + str(hr) + ":" + str(min)
        return statusStr

class Switch(): 
    def __init__(self):
        self.__key = "1"
        self.__latch = False 
        self.__latchState = 0
        self.__timer = 0 
        self.__release = True
        self.__interval = 0.0    # milliseconds 
        self.active = True

    def getKey(self): 
        return self.__key 
    
    def getActive(self): 
        return self.active

    def setConfig(self, key, latch=False, interval=0.0, release=False, enable=True):
        # release old key if currently held down
        self.releaseKey(force=True) 
        self.__latchState = 0
        self.active = enable

        self.__key = key 
        self.__latch = latch 
        self.__interval = interval
        self.__release = release 
    
    def activate(self):
        self.active = True 

    def deactivate(self): 
        self.active = False
    
    def pressKey(self, force=False): 
        if self.active or force: 
            if self.__release: 
                ue.keyDown(self.__key)
            else: 
                ue.typewrite(self.__key, interval=self.__interval)
    
    def releaseKey(self, force=False): 
        if self.active or force: 
            if self.__release:
                ue.keyUp(self.__key)
        


if __name__ == '__main__':
    print("I never developed self-test, but if I did they would go here.")

    pt = ParsingTools()

    print("Testing macToString")
    print(pt.macToString(b'023430'))
    print("Testing getModuleIDfromTopic")
    print(pt.getIDfromTopic("encoder/12:23:32:32:32/health/ota"))
    print("Testing getFieldfromTopic")
    print(pt.getFieldfromTopic("encoder/12:23:32:32:32/health/ota"))
