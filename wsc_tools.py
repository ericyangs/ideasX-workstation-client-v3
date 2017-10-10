import  pyautogui as ue

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
        self.releaseKey() 
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
    
    def pressKey(self): 
        if self.__release: 
            ue.keyDown(self.__key)
        else: 
            ue.typewrite(self.__key, interval=self.__interval)
    
    def releaseKey(self): 
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
