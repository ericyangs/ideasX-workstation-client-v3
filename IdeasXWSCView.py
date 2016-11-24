import sys
import time
import sip
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
from ideasxdevice import Ui_IdeasXDevice
from IdeasXWSCBackend import IdeasXWSCNetworkThread
from ParsingTools import ParsingTools
from encoderconfigurationdialog import Ui_SwitchConfigDialog


class IdeasXSwitchDialog(QtWidgets.QDialog):
    
    def __init__(self, switch, assignedKey): 
        super(IdeasXSwitchDialog, self).__init__()
        self.__ui = Ui_SwitchConfigDialog()
        self.__ui.setupUi(self)
        self.__ui.buttonApply.clicked.connect(self.submitOnClose)
        self.key = assignedKey[0]
        self.enable = assignedKey[1]
        self.switch = switch
        
        self.__ui.checkSwitchEnable.setChecked(self.enable)
        self.__ui.lineSwitchKey.setText(self.key)
        
    def submitOnClose(self):
        self.key = self.__ui.lineSwitchKey.text() 
        self.enable = self.__ui.checkSwitchEnable.isChecked()
        self.accept()

class IdeasXDeviceManager():
    def __init__(self, deviceClass, wsc): 
        self.__devices = {} 
        self.__deviceClass = deviceClass
        self.__deviceLayout = QtWidgets.QVBoxLayout()
        self.__deviceLayout.setAlignment(QtCore.Qt.AlignTop)
        self.__deviceLayout.setContentsMargins(9, 0, 9, 0)
        self.__deviceLayout.setSpacing(0)
        self.__wsc = wsc
          
    def refreshDevices(self, devices):
        for deviceMAC in devices.keys(): 
            if deviceMAC in self.__devices.keys(): 
                print("Updating Device")
                self.__devices[deviceMAC].updateDevice(devices[deviceMAC])
            else: 
                print("Adding Device")
                self.__devices[deviceMAC] = self.__deviceClass(devices[deviceMAC], self.__wsc)
                self.__deviceLayout.addWidget(self.__devices[deviceMAC])
        for deviceMAC in list(self.__devices.keys()): 
            if deviceMAC not in devices.keys(): 
                print("Removing Device")
                self.removeDevice(deviceMAC)
                
    def removeDevice(self, deviceMAC): 
        self.__deviceLayout.removeWidget(self.__devices[deviceMAC])
        sip.delete(self.__devices[deviceMAC])
        self.__devices.pop(deviceMAC)
        
    def returnLayout(self):
        return self.__deviceLayout
        
    def filterDevices(self, searchPhase):
        print("This currently doesn't work")
        
    def printDevices(self):
        print(self.__devices)

class IdeasXEncoder(QtWidgets.QWidget):
    sendCommand = QtCore.pyqtSignal(['QString'], name='sendCommand')
    
    def __init__(self, encoder, wsc): 
        # This should become a static variable for the class
        self.__pathToIcon = {'network': './icon/network/', 
                             'battery': './icon/battery/', 
                             'battery_charging': './icon/battery/',
                             'switch': './icon/switch/'
                            }
        self.__icon = {'network': ['network-wireless-offline-symbolic.png',
                                   'network-wireless-signal-weak-symbolic.png',
                                   'network-wireless-signal-ok-symbolic.png',
                                   'network-wireless-signal-good-symbolic.png',
                                   'network-wireless-signal-excellent-symbolic.png'],
                        'battery': ['battery-empty-symbolic.png', 
                                    'battery-caution-symbolic.png',
                                    'battery-low-symbolic.png', 
                                    'battery-good-symbolic.png',
                                    'battery-full-symbolic.png'],
                        'battery_charging': ['battery-empty-charging-symbolic.png', 
                                             'battery-caution-charging-symbolic.png', 
                                             'battery-low-charging-symbolic.png', 
                                             'battery-good-charging-symbolic.png', 
                                             'battery-full-charged-symbolic.png'],
                        'switch': ['switch-one-enabled.png', 
                                   'switch-one-disabled.png', 
                                   'switch-two-enabled.png', 
                                   'switch-two-disabled.png', 
                                   'switch-adpative-enabled.png', 
                                   'switch-adaptive-disabled.png']
                       }
        self.__deviceType = 'encoder'
        self.__wsc = wsc
        # Setup UI components
        super(IdeasXEncoder, self).__init__()
        self.__ui = Ui_IdeasXDevice()
        self.__ui.setupUi(self)
        self._parserTools = ParsingTools()
        self.updateDevice(encoder)        

        self.setupMenu()
        self.__ui.buttonActivate.clicked.connect(self.activateEncoder)
        self.__ui.buttonSwitchOne.clicked.connect(lambda: self.openSwitchDialog(self.__wsc.keyEmulator.switchOne,
                                                                                 self.__wsc.keyEmulator.getAssignedKey(self.__strModuleID, self.__wsc.keyEmulator.switchOne)))
        self.__ui.buttonSwitchTwo.clicked.connect(lambda: self.openSwitchDialog(self.__wsc.keyEmulator.switchTwo,
                                                                                self.__wsc.keyEmulator.getAssignedKey(self.__strModuleID, self.__wsc.keyEmulator.switchTwo)))
    
    def openSwitchDialog(self, switch, assignedKey):
        dialog = IdeasXSwitchDialog(switch, assignedKey)
        if dialog.exec_():                
            if dialog.key != None or len(dialog.key) == 1: 
                self.__wsc.keyEmulator.assignKey(self.__strModuleID, dialog.switch, dialog.key, dialog.enable)
                
                # Think of a better way to do this
                if dialog.enable: 
                    if switch == self.__wsc.keyEmulator.switchOne: 
                        self.__ui.buttonSwitchOne.setIcon(self.setupSwitchIcon(self.__icon['switch'][0]))
                        
                    if switch == self.__wsc.keyEmulator.switchTwo:
                        self.__ui.buttonSwitchTwo.setIcon(self.setupSwitchIcon(self.__icon['switch'][2]))
                        
                    if switch == self.__wsc.keyEmulator.switchAdaptive:
                        self.__ui.buttonSwitchAdaptive.setIcon(self.setupSwitchIcon(self.__icon['switch'][4]))
                        
                if dialog.enable == False: 
                    if switch == self.__wsc.keyEmulator.switchOne: 
                        self.__ui.buttonSwitchOne.setIcon(self.setupSwitchIcon(self.__icon['switch'][1]))
                        
                    if switch == self.__wsc.keyEmulator.switchTwo:
                        self.__ui.buttonSwitchTwo.setIcon(self.setupSwitchIcon(self.__icon['switch'][3]))
                        
                    if switch == self.__wsc.keyEmulator.switchAdaptive:
                        self.__ui.buttonSwitchAdaptive.setIcon(self.setupSwitchIcon(self.__icon['switch'][5]))
                        
    def setupSwitchIcon(self, path):
        icon = QtGui.QIcon()
        iconPath = self.__pathToIcon['switch']
        iconPath = iconPath + path
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon
              
    def setupMenu(self):
        shutdownAction = QtWidgets.QAction('Shutdown Encoder', self)
        shutdownAction.triggered.connect(lambda: self.__wsc.shutdownDevice(self.__strModuleID, None))
        
        deviceMenu = QtWidgets.QMenu()
        #deviceMenu.addSection("General Actions")
        #deviceMenu.addAction("Pair Encoder with Actuator")
        #deviceMenu.addAction("Train Adaptive Switch")
        #deviceMenu.addAction("Configure Module")
        deviceMenu.addSection("Encoder Commands")
        deviceMenu.addAction(shutdownAction)
        #deviceMenu.addAction("Restart Encoder")
       # deviceMenu.addAction("Update Firmware")
        
        self.__ui.buttonMenu.setPopupMode(2)
        self.__ui.buttonMenu.setMenu(deviceMenu)
        self.__ui.buttonMenu.setStyleSheet("* { padding-right: 3px } QToolButton::menu-indicator { image: none }")    
        
    def activateEncoder(self):
        if self.__ui.buttonActivate.text() == "Activate":
            print("Activating Encoder: " + self.__ui.labelModuleID.text())
            self.__ui.buttonActivate.setText("Deactivate")
        else: 
            print("Deactivating Encoder: " + self.__ui.labelModuleID.text())
            self.__ui.buttonActivate.setText("Activate")
            self.sendCommand.emit(self.__ui.labelModuleID.text())
        
    def updateDevice(self, encoder):      
        self.__rssi = encoder['rssi']
        self.__soc = self._parserTools.calculateSOC(encoder['soc'])
        self.__vcell = self._parserTools.calculateVCell(encoder['vcell'])
        self.__strModuleID = self._parserTools.macToString(encoder['module_id'])
        self.__updateTime = encoder['time']
        
        self.setModuleID(self.__strModuleID)
        self.setSOCIcon(self.__soc)
        self.setRSSIIcon(self.__rssi)
        self.setStatusTime(self.__updateTime)

    def setModuleID(self, strModuleID):      
        self.__ui.labelModuleID.setText(strModuleID)

    def setSOCIcon(self, soc):
        if soc >= 75: 
            batteryIcon = 4
        elif soc >= 50 and soc < 75: 
            batteryIcon = 3
        elif soc >= 25 and soc < 50: 
            batteryIcon = 2 
        elif soc >=10 and soc < 25: 
            batteryIcon = 1
        elif soc < 10: 
            batteryIcon = 0 
        batteryIcon = self.__pathToIcon['battery']+self.__icon['battery'][batteryIcon]
        self.__ui.labelBattery.setPixmap(QtGui.QPixmap(batteryIcon))
        self.__ui.labelBattery.setToolTip(str(soc) + "%")
        
    def setStatusTime(self, updateTime):
        # set last update time or date
        lastUpdate = time.ctime(updateTime).split(" ")
        currentTime = time.ctime().split(" ")
        if currentTime[1] != lastUpdate[1] or currentTime[2] != lastUpdate[2] or currentTime[4] != lastUpdate[4]: 
            lastUpdate = lastUpdate[1] + " " + lastUpdate[2] + " " + lastUpdate[4]
        else: 
            lastUpdate = lastUpdate[3]
        self.__ui.labelStatus.setText("Last Update: " + lastUpdate)
        
    def setRSSIIcon(self, rssi): 
        # set rssi icon
        if rssi >= -50: 
            rssiIcon = 4
        elif rssi >= -60 and rssi < -50: 
            rssiIcon = 3 
        elif rssi >= -70 and rssi < -60: 
            rssiIcon = 2 
        elif rssi < -70: 
            rssiIcon = 1  
        rssiIcon = self.__pathToIcon['network'] + self.__icon['network'][rssiIcon]  
        self.__ui.labelSignal.setPixmap(QtGui.QPixmap(rssiIcon))
        self.__ui.labelSignal.setToolTip(str(rssi) + " dBm")
            


class IdeasXMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(IdeasXMainWindow, self).__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        p = self.__ui.contentEncoder.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.__ui.contentEncoder.setPalette(p)

    def setEncoderLayout(self, layout):
        self.__ui.contentEncoder.setLayout(layout)
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon/logo/ideasx.png'))
    mainWindow = IdeasXMainWindow()
    wsc = IdeasXWSCNetworkThread()
    encoderManager = IdeasXDeviceManager(IdeasXEncoder, wsc)
    mainWindow.setEncoderLayout(encoderManager.returnLayout())
    wsc.encoderUpdate.connect(encoderManager.refreshDevices)
    wsc.guiStartWorkstationClient('ideasx.duckdns.org')
    
    #timer = QtCore.QTimer()
    #timer.timeout.connect(mainWindow.hideEncoder)
    #timer.start(1000)
    #time.sleep(0.5)
    
    mainWindow.show()
    sys.exit(app.exec_())
    