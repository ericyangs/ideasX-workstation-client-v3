class ParsingTools():
    def macToString(self, mac_bytes):
        ''' Convert uint8 byte string to "XX:XX:XX:XX:XX" 
        '''
        mac_str = ""
        for byte in mac_bytes: 
            mac_str = mac_str + format(byte, 'x') + ':'
        return mac_str[:-1].format('utf-8')
            
    def calculateVCell(self, raw_Vcell):
        return raw_Vcell*1.25e-3
    
    def calculateSOC(self, raw_SOC):
        return raw_SOC.to_bytes(2, 'big')[0]
    

if __name__ == '__main__':
    print("I never developed self-test, but if I did they would go here.")
    
    pt = ParsingTools()
    
    print("Testing macToString")
    print(pt.macToString(b'023430'))
    