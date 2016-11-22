'''
Title: IdeasXDatabaseManager Class
Author: Tyler Berezowsky 
Description: The purpose of this class is to parse the general portions 
(non-extended) portions of HealthMessages from the IdeasX system. Parshing 
completed by auto-generated code from the Google Protocols project. Once 
parsed, the information is stored into an SQLite DB. 

Requirements: 
- This class needs to be expandable for different device types.

ToDo: 
- Code should be updated to utilize QSqlQuery.execBatch
'''

from PyQt5 import QtSql
import time 
import os
try:     
    from protocolbuffers import IdeasXMessages_pb2 as IdeasXMessages
except ImportError: 
    print("The python classes for IdeasX are missing. Try running the Makefile in" +
            "ideasX-messages.")
            

class IdeasXDatabaseManager():
    def __init__(self, database_filename='IdeasX.db'): 
        ''' Attempt to initialize database.
        '''
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(database_filename)
        db_open = self.db.open()
        # check if DB exists 
        #if not os.path.isfile('./'+database_filename):
        if True:    
            if db_open:
                self.query = QtSql.QSqlQuery() 
                self.query.exec("CREATE TABLE encoder("                 + 
                                    "module_id char(17) primary key, "  +
                                    "state_of_charge int, "             +
                                    "battery_voltage real, "            +
                                    "rssi int, "                        +
                                    "firmware_version int, "            + 
                                    "hardware_version int, "            +
                                    "ssid varchar(33), "                +
                                    "bssid varchar(33), "               +
                                    "active bool, "                     +
                                    "charging bool, "                   +
                                    "low_battery bool, "                +
                                    "ota bool);")       
                
                self.printError("Created database")
            else: 
                self.printError("Failed to open/create database")
                # system exit
        else:
            self.printError("Database already exists")
            self.query = QtSql.QSqlQuery() 

            
        # initalize parsers
        self.healthMessage = IdeasXMessages.HealthMessage()
        #self.dataMessageParser = IdeasXMessages.DataMessage()
        #self.commandMessageParser = IdeasXMessages.CommandMessage()
            
    def printError(self, error_msg):
        print("IdeasX Database Manager Error: " + error_msg)

    def printMsg(self, msg):
        print("IdeasX Database Manager: " + msg)
            
    def parseHealthMessage(self, msg):
        self.healthMessage.ParseFromString(msg)
        
        flagOTA = 0 
        flagCharging = 0 
        flagLb = 0 
        flagActive = 0 
        if self.healthMessage.state.ota: 
            flagOTA = 1
        if self.healthMessage.state.charging:
            flagCharging = 1 
        if self.healthMessage.state.lb: 
            flagLb = 1 
        if self.healthMessage.state.active: 
            flagActive = 1
            
        update = self.query.exec("SELECT 1 FROM encoder WHERE module_id ='"+self.macToString(self.healthMessage.module_id)+"';")
        if self.query.next():
            update = self.query.exec_("UPDATE encoder "+ 
                             "SET state_of_charge="+str(self.calculateSOC(self.healthMessage.soc))+","+
                             "battery_voltage="+str(self.calculateVCell(self.healthMessage.vcell))+","+
                             "firmware_version="+str(self.healthMessage.firmware)+","+
                             "hardware_version="+str(self.healthMessage.hardware_version)+","+ 
                             "rssi="+str(self.healthMessage.rssi)+","+
                             "ssid='"+self.healthMessage.ssid+"',"+
                             "bssid='"+self.healthMessage.bssid+"',"+
                             "active="+str(flagActive)+","+ 
                             "ota="+str(flagOTA)+","+ 
                             "charging="+str(flagCharging)+","+ 
                             "low_battery="+str(flagLb)+" "+
                             "WHERE module_id='"+self.macToString(self.healthMessage.module_id)+"';")
            self.printMsg("Updated existing module fields " + self.macToString(self.healthMessage.module_id))

            
        else:
            update = self.query.exec_("INSERT INTO encoder VALUES("+
                                     "'"+self.macToString(self.healthMessage.module_id)+"',"+
                                     str(self.calculateSOC(self.healthMessage.soc))+","+
                                     str(self.calculateVCell(self.healthMessage.vcell))+","+
                                     str(self.healthMessage.rssi)+","+
                                     str(self.healthMessage.firmware)+","+
                                     str(self.healthMessage.hardware_version)+","+
                                     "'"+self.healthMessage.ssid+"',"+
                                     "'"+self.healthMessage.bssid+"',"+
                                     str(flagActive)+","+
                                     str(flagCharging)+","+
                                     str(flagLb)+","+
                                     str(flagOTA)+
                                     ");")
            self.printMsg("Created new module " + self.macToString(self.healthMessage.module_id))
        if update == False:
            self.printError("SQL operation failed!")
    
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
        

    def clearDatabase(self):
        self.printError("Failed to delete database")
        
        
if __name__ == '__main__':
    dbm = IdeasXDatabaseManager()
    msg = IdeasXMessages.HealthMessage()
    msg.module_id = bytes("1113321", 'utf-8')
    msg.rssi = -56 
    msg.soc = 89 
    msg.vcell = 54323
    msg.ssid = "Icaraus"
    msg.state.ota = False 
    msg.state.lb = False 
    msg.state.charging = False
    msg.state.active = False
    msg.auth = 0 
    msg.firmware = 123
    msg.hardware_version = 1 
    msg.rom = 0
    str_msg = msg.SerializeToString()
    
    dbm.parseHealthMessage(str_msg)
    
        
            # exit program 