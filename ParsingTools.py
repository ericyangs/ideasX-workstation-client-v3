class ParsingTools():
    def macToString(self, mac_bytes):
        ''' Convert uint8 byte string to "XX:XX:XX:XX:XX" 
        '''
        mac_str = ""
        for byte in mac_bytes: 
            mac_str = mac_str + format(byte, '02x') + ':'
        return mac_str[:-1].format('utf-8')
            
    def calculateVCell(self, raw_Vcell):
        return raw_Vcell*1.25e-3
    
    def calculateSOC(self, raw_SOC):
        return raw_SOC.to_bytes(2, 'big')[0]
    
    def getModuleIDfromTopic(self, topic):
        return topic.split('/')[2]
        
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
    

if __name__ == '__main__':
    print("I never developed self-test, but if I did they would go here.")
    
    pt = ParsingTools()
    
    print("Testing macToString")
    print(pt.macToString(b'023430'))
    