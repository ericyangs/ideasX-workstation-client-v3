import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from mainwindow import Ui_MainWindow
from ideasxdevice import Ui_IdeasXDevice
from WorkstationClientClass import WorkstationClientClass
from ParsingToolsClass import ParsingTools


def generateMACID():
    import numpy as np
    macID = np.random.randint(255, size=5)
    macStr = ""
    for val in macID: 
        macStr = macStr+ format(val, 'x') + ":" 
    return macStr[:-1]

def generateRSSI():
    import numpy as np 
    rssi = np.random.randint(80)
    rssiStr = "RSSI:  -" + str(rssi) + "dBm"
    return rssiStr 

def generateSOC():
    import numpy as np
    soc = np.random.randint(100)
    socStr = "Battery:  " + str(soc) + "%"
    return socStr
    
def generateStatus():
    import numpy as np 
    hr = np.random.randint(12) + 1
    min = np.random.randint(60)
    ampm = np.random.randint(1)
    statusStr = "Last Update: " + str(hr) + ":" + str(min)
    return statusStr

class IdeasXEncoder(QtWidgets.QWidget):
    def __init__(self, wsc, encoder): #, encoderID, encoderRSSI, encoderBattery, encoderStatus):
        super(IdeasXEncoder, self).__init__()
        self.ui = Ui_IdeasXDevice()
        self.ui.setupUi(self)
#         self.ui.labelModuleID.setText(encoderID)
#         self.ui.labelRSSI.setText(encoderRSSI)
#         self.ui.labelBattery.setText(encoderBattery)
#         self.ui.labelStatus.setText("I don't really have something here yet...")
        self.parserTools = ParsingTools()
        self.wsc = wsc

        self.ui.labelModuleID.setText(self.parserTools.macToString(encoder['module_id']))
        self.ui.labelRSSI.setText("RSSI: " + str(encoder['rssi']) + "dBm")
        self.ui.labelBattery.setText("Battery: " + str(self.parserTools.calculateSOC(encoder['soc'])) + "%" +
                                     " (" + str(round(self.parserTools.calculateVCell(encoder['vcell']), 3)) +"V)")
        self.ui.labelStatus.setText("Last Update: " + time.ctime(encoder['time']))
        self.ui.buttonActivate.clicked.connect(self.activateEncoder)
        
        deviceMenu = QtWidgets.QMenu()
        deviceMenu.addSection("General Actions")
        deviceMenu.addAction("Pair Encoder with Actuator")
        deviceMenu.addAction("Train Adaptive Switch")
        deviceMenu.addAction("Configure Module")
        deviceMenu.addSection("Encoder Commands")
        deviceMenu.addAction("Shutdown Encoder")
        deviceMenu.addAction("Restart Encoder")
        deviceMenu.addAction("Update Firmware")
        
        #deviceMenu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ui.buttonMenu.setPopupMode(2)
        self.ui.buttonMenu.setMenu(deviceMenu)
        self.ui.buttonMenu.setStyleSheet("* { padding-right: 3px } QToolButton::menu-indicator { image: none }")
#         self.ui.buttonMenu.setToolbarButtonSytel
        
        
             
    def activateEncoder(self):
        if self.ui.buttonActivate.text() == "Activate":
            print("Activating Encoder: " + self.ui.labelModuleID.text())
            self.ui.buttonActivate.setText("Deactivate")
        else: 
            print("Deactivating Encoder: " + self.ui.labelModuleID.text())
            self.ui.buttonActivate.setText("Activate")
        
#         self.widgetText = QtWidgets.QLabel(generateMACID())
#         self.widgetButton = QtWidgets.QPushButton("Activate")
#         self.layout = QtWidgets.QHBoxLayout()
#         self.layout.addWidget(self.widgetText)
#         self.layout.addWidget(self.widgetButton)
#         self.setLayout(self.layout)
#         font = QtGui.QFont()
#         font.setFamily("Roboto Condensed")
#         font.setPointSize(20)
#         font.setItalic(False)
#         self.widgetText.setFont(font)
    

class IdeasXMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(IdeasXMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        'module_id', b'\x18\xfe4\xf1\xf2\x8d'
        self.encoders = {'23:4d:12:2a:ad': {'module_id': b'\x18\xfe4\xf1\xf2\x8d', 'rssi': -54, 'soc': 32432}, 
                         '43:3d:12:3a:ad': {'module_id': b'\x18\xfe4\xf1\xf2\x8d', 'rssi': -73, 'soc': 24243}}
        
#         self.wsc = WorkstationClientClass()
#         self.wsc.guiStartWorkstationClient('10.41.0.1')
#         self.wsc.refreshCallBack(self.refreshList)
        
        #self.ui.searchEncoder.textChanged.connect(self.filterEncoders)
#         itemN = QtWidgets.QListWidgetItem()
#         widget = IdeasXEncoder()
#         itemN.setSizeHint(widget.minimumSize())
#         self.ui.listEncoder.addItem(itemN)
#         self.ui.listEncoder.setItemWidget(itemN, widget)
        
        #widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        #widget.setLayout(widgetLayout)
        
#         self.widgetIndex = []
#         self.widgetNames = []
#         self.itemIndex = []
#         for i in range(100):
#             self.itemIndex.append(QtWidgets.QListWidgetItem())
#             self.widgetIndex.append(IdeasXEncoder())
#             itemN = self.itemIndex[i]
#             widget = self.widgetIndex[i]
#             itemN.setSizeHint(widget.minimumSize())
#          
#             #widget = IdeasXEncoder()
#             self.ui.listEncoder.addItem(itemN)
#             self.ui.listEncoder.setItemWidget(itemN, widget)
#             self.widgetNames.append(widget.ui.labelModuleID.text())
#             
#         print("List of Encoder IDs: ")
#         print(self.widgetNames)
        self.wsc = WorkstationClientClass()
        #self.wsc.attachRefreshCallback(self.generateEncoderList)
        self.wsc.guiStartWorkstationClient('ideasx.duckdns.org')
        #self.generateEncoderList()
        
    def generateEncoders(self):
        self.widgetIndex = []
        self.itemIndex = []
        for i in range(100):
            itemN = QtWidgets.QListWidgetItem()
            self.widgetIndex.append(IdeasXEncoder(self.wsc))
            widget = self.widgetIndex[i]
            itemN.setSizeHint(widget.minimumSize())
         
            #widget = IdeasXEncoder()
            self.ui.listEncoder.addItem(itemN)
            self.ui.listEncoder.setItemWidget(itemN, widget)
#             
    def generateEncoder(self, wsc, encoder):
        itemN = QtWidgets.QListWidgetItem()
        #self.widgetIndex.append(IdeasXEncoder())
        widget = IdeasXEncoder(wsc, encoder)#self.widgetIndex[-1]
        itemN.setSizeHint(widget.minimumSize())
        self.ui.listEncoder.addItem(itemN)
        self.ui.listEncoder.setItemWidget(itemN, widget)
        return widget
        
    def clearEncoders(self):
        self.ui.listEncoder.clear()
        self.widgetIndex = []
        
    def generateEncoderList(self):
        self.clearEncoders()
        for encoderMAC in self.wsc.encoders.keys():
            self.generateEncoder(self.wsc, self.wsc.encoders[encoderMAC])
            
    def filterEncoders(self):
        searchInput = self.ui.searchEncoder.text()
        if searchInput == "":
            print("Search field is clear")
            for item in self.itemIndex:
                self.ui.listEncoder.setItemHidden(item, False)
        else:
            for item in self.itemIndex: 
                self.ui.listEncoder.setItemHidden(item, False)
            print("Seaching based on "+ searchInput)
            # hid all items 
            # make only items in view searchable 
            
    def encoderSettingsDialog(self):
        print("Open Settings Dialog")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon/ideasx.png'))
    mainWindow = IdeasXMainWindow()
    mainWindow.show()
    
    timer = QtCore.QTimer()
    timer.timeout.connect(mainWindow.generateEncoderList)
    timer.start(1000)
    time.sleep(2)
    mainWindow.generateEncoderList()
     
    sys.exit(app.exec_())
    