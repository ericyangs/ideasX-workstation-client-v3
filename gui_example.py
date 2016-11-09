import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from mainwindow import Ui_MainWindow
from ideasxdevice import Ui_IdeasXDevice

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
    def __init__(self):
        super(IdeasXEncoder, self).__init__()
        self.ui = Ui_IdeasXDevice()
        self.ui.setupUi(self)
        self.ui.labelModuleID.setText(generateMACID())
        self.ui.labelRSSI.setText(generateRSSI())
        self.ui.labelBattery.setText(generateSOC())
        self.ui.labelStatus.setText(generateStatus())
        self.ui.buttonActivate.clicked.connect(self.activateEncoder)
        
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
        
        #self.ui.searchEncoder.textChanged.connect(self.filterEncoders)
#         itemN = QtWidgets.QListWidgetItem()
#         widget = IdeasXEncoder()
#         itemN.setSizeHint(widget.minimumSize())
#         self.ui.listEncoder.addItem(itemN)
#         self.ui.listEncoder.setItemWidget(itemN, widget)
        
        #widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        #widget.setLayout(widgetLayout)
        
        self.widgetIndex = []
        self.widgetNames = []
        self.itemIndex = []
        for i in range(100):
            self.itemIndex.append(QtWidgets.QListWidgetItem())
            self.widgetIndex.append(IdeasXEncoder())
            itemN = self.itemIndex[i]
            widget = self.widgetIndex[i]
            itemN.setSizeHint(widget.minimumSize())
         
            #widget = IdeasXEncoder()
            self.ui.listEncoder.addItem(itemN)
            self.ui.listEncoder.setItemWidget(itemN, widget)
            self.widgetNames.append(widget.ui.labelModuleID.text())
            
        print("List of Encoder IDs: ")
        print(self.widgetNames)
        
    def generateEncoders(self):
        self.widgetIndex = []
        self.itemIndex = []
        for i in range(100):
            itemN = QtWidgets.QListWidgetItem()
            self.widgetIndex.append(IdeasXEncoder())
            widget = self.widgetIndex[i]
            itemN.setSizeHint(widget.minimumSize())
         
            #widget = IdeasXEncoder()
            self.ui.listEncoder.addItem(itemN)
            self.ui.listEncoder.setItemWidget(itemN, widget)
#             
    def generateEncoder(self):
        itemN = QtWidgets.QListWidgetItem()
        #self.widgetIndex.append(IdeasXEncoder())
        widget = IdeasXEncoder()#self.widgetIndex[-1]
        itemN.setSizeHint(widget.minimumSize())
        self.ui.listEncoder.addItem(itemN)
        self.ui.listEncoder.setItemWidget(itemN, widget)
        
    def clearEncoders(self):
        self.ui.listEncoder.clear()
        self.widgetIndex = []
        
    def refreshList(self):
        #self.clearEncoders()
        for widget in self.widgetIndex: 
            widget.ui.labelBattery.setText(generateSOC())
            widget.ui.labelStatus.setText(generateStatus())
            widget.ui.labelRSSI.setText(generateRSSI())
            
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
    app.setWindowIcon(QtGui.QIcon('icon/ideasx2.png'))
    mainWindow = IdeasXMainWindow()
    mainWindow.show()
    
    timer = QtCore.QTimer()
    timer.timeout.connect(mainWindow.refreshList)
    timer.start(1000)
    
    sys.exit(app.exec_())
    