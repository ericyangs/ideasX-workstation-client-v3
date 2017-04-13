
'''
IdeasXWSCView.py 

TODO: Fix activate / deactivate functionality [done]
TODO: Fix subscribe / unsubscribe functionality in backend [done]
TODO: Develop queue message thinger for sub unsub with feedback from backend

TODO: Develop structure for creating alias for device
TODO: Develop structure for saving information into backend

'''
import sys
import time
import sip
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt.mainwindow2 import Ui_MainWindow
from pyqt.ideasxdevice import Ui_IdeasXDevice
from IdeasXWSCBackend import IdeasXWSCNetworkThread
from pyqt.encoderconfigurationdialog import Ui_SwitchConfigDialog
from pyqt.devicedialog import Ui_Dialog
from ParsingTools import ParsingTools


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
        
class IdeasXDeviceInformationDialog(QtWidgets.QDialog):
    newDeviceName = QtCore.pyqtSignal(['QString'], name='newDeviceName')
    
    def __init__(self):
        super(IdeasXDeviceInformationDialog, self).__init__()
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)
        self.__ui.lineAlias.textEdited.connect(lambda: self.newDeviceName.emit(self.__ui.lineAlias.text()))
        
    def updateDisplay(self, encoder):
        self.__ui.labelBatteryCapacity.setText(str(encoder['soc']))
        self.__ui.labelBatteryVoltage.setText(str(encoder['vcell']))
        self.__ui.labelLowBattery.setText(str(encoder['lb']))
        self.__ui.labelChargeState.setText('N/A')
        
        self.__ui.labelActiveFlag.setText('N/A')
        self.__ui.labelAliveFlag.setText(str(encoder['alive'])) 
        self.__ui.labelFirmwareVersion.setText(str(encoder['firmware_version'])) 
        self.__ui.labelHardwareVersion.setText(str(encoder['hardware_version'])) 
        self.__ui.labelOTAFlag.setText(str(encoder['ota']))
        self.__ui.labelROMSlot.setText(str(encoder['rom'])) 
        
        self.__ui.labelMAC.setText(str(encoder['module_id']))
        self.__ui.labelRSSI.setText(str(encoder['rssi'])) 
        self.__ui.labelSSID.setText(encoder['ssid']) 
        
    

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
        for deviceMAC in list(devices.keys()): 
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
    activateDevice = QtCore.pyqtSignal(['QString', 'QString'], name='deactivateDevice')
    deactivateDevice = QtCore.pyqtSignal(['QString', 'QString'], name='activateDevice')
    __pathToIcon = {'network': './icon/network/', 
                     'battery': './icon/battery/', 
                     'battery_charging': './icon/battery/',
                     'switch': './icon/switch/'
                    }
    __icon = {'network': ['network-wireless-offline-symbolic.png',
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
                               'switch-adaptive-enabled.png', 
                               'switch-adaptive-disabled.png']
                   }
    __deviceType = '/encoder/'

    
    def __init__(self, encoder, wsc): 
        self.__deviceName = None
        self.__wsc = wsc
        
        # Setup UI components
        super(IdeasXEncoder, self).__init__()
        self.__ui = Ui_IdeasXDevice()
        self.__ui.setupUi(self)
        self._parserTools = ParsingTools()
        self.updateDevice(encoder)        
        self.updateSwitchIcons()
        
        # Setup Signals
        self.setupMenu()
        self.__ui.buttonActivate.clicked.connect(self.activateEncoder)
        self.__ui.buttonSwitchOne.clicked.connect(lambda: self.openSwitchDialog(self.__wsc.keyEmulator.switchOne,
                                                                                 self.__wsc.keyEmulator.getAssignedKey(self.__strModuleID, self.__wsc.keyEmulator.switchOne)))
        self.__ui.buttonSwitchTwo.clicked.connect(lambda: self.openSwitchDialog(self.__wsc.keyEmulator.switchTwo,
                                                                                self.__wsc.keyEmulator.getAssignedKey(self.__strModuleID, self.__wsc.keyEmulator.switchTwo)))
        self.activateDevice.connect(self.__wsc.activateEncoder)
        self.deactivateDevice.connect(self.__wsc.deactivateEncoder)
        
    def openDeviceInformation(self):
        dialog = IdeasXDeviceInformationDialog()
        dialog.updateDisplay(self.__wsc.encoders[self.__strModuleID])
        dialog.newDeviceName.connect(self.setDeviceAlisas)
        dialog.exec()
    
    def openSwitchDialog(self, switch, assignedKey):
        dialog = IdeasXSwitchDialog(switch, assignedKey)
        if dialog.exec_():                
            if dialog.key != None and len(dialog.key) == 1: 
                self.__wsc.keyEmulator.assignKey(self.__strModuleID, dialog.switch, dialog.key, dialog.enable)
                self.updateSwitchIcons()
                        
    def setupSwitchIcon(self, path):
        icon = QtGui.QIcon()
        iconPath = self.__pathToIcon['switch']
        iconPath = iconPath + path
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon
              
    def setupMenu(self):
        shutdownAction = QtWidgets.QAction('Shutdown Encoder', self)
        resetAction = QtWidgets.QAction("Reset Encoder", self)
        testKeysAction = QtWidgets.QAction("Test Keys", self)
        openInfoAction = QtWidgets.QAction("Device Information", self)
        startOTAAction = QtWidgets.QAction("OTA Update", self)

        testKeysAction.triggered.connect(self.testKeys)
        openInfoAction.triggered.connect(self.openDeviceInformation)
        startOTAAction.triggered.connect(lambda: self.__wsc.updateDevice(self.__strModuleID, None))
        shutdownAction.triggered.connect(lambda: self.__wsc.shutdownDevice(self.__strModuleID, None))
        resetAction.triggered.connect(lambda: self.__wsc.resetDevice(self.__strModuleID, None))

                
        deviceMenu = QtWidgets.QMenu()
        deviceMenu.addAction(shutdownAction)
        deviceMenu.addAction(resetAction)
        deviceMenu.addAction(openInfoAction)
        deviceMenu.addSection("Engineering Tools")
        deviceMenu.addAction(testKeysAction)
        deviceMenu.addAction(startOTAAction)
        
        self.__ui.buttonMenu.setPopupMode(2)
        self.__ui.buttonMenu.setMenu(deviceMenu)
        self.__ui.buttonMenu.setStyleSheet("* { padding-right: 3px } QToolButton::menu-indicator { image: none }")    
        
    def activateEncoder(self):
        if self.__ui.buttonActivate.text() == "Activate":
            print("Activating Encoder: " + self.__ui.labelModuleID.text())
            self.activateDevice.emit(self.__strModuleID, self.__deviceType)
            self.__ui.buttonActivate.setText("Deactivate")
        else: 
            print("Deactivating Encoder: " + self.__ui.labelModuleID.text())
            self.deactivateDevice.emit(self.__strModuleID, self.__deviceType)
            self.__ui.buttonActivate.setText("Activate")
        
    def updateDevice(self, encoder):      
        self.__rssi = encoder['rssi']
        self.__soc = self._parserTools.calculateSOC(encoder['soc'])
        self.__vcell = self._parserTools.calculateVCell(encoder['vcell'])
        self.__strModuleID = self._parserTools.macToString(encoder['module_id'])
        self.__updateTime = encoder['time']
        self.__ota = encoder['ota']
        
        if self.__deviceName == None:
            self.setModuleID(self.__strModuleID)
        self.setSOCIcon(self.__soc)
        self.setRSSIIcon(self.__rssi)
        self.setStatusTime(self.__updateTime)
        self.setOTAIcon(self.__ota)
        
    def setOTAIcon(self, ota):
        if ota: 
            self.__ui.labelOTA.show()
        else: 
            self.__ui.labelOTA.hide()

    def setModuleID(self, strModuleID):      
        self.__ui.labelModuleID.setText(strModuleID)
        
    def setDeviceAlisas(self, label):
        self.__deviceName = label
        if label != None or label != "": 
            self.__ui.labelModuleID.setText(label)
        else: 
            self.__ui.labelModuleID.setText(self.__strModuleID)

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
        lastUpdate = time.ctime(updateTime).replace("  ", " ").split(" ")
        currentTime = time.ctime().replace("  ", " ").split(" ")
        if currentTime[1] != lastUpdate[1] or currentTime[2] != lastUpdate[2] or currentTime[4] != lastUpdate[4]: 
            lastUpdate = lastUpdate[1] + " " + lastUpdate[2] + " " + lastUpdate[4]
        else: 
            lastUpdate = lastUpdate[3]
        self.__ui.labelStatus.setText("Last Update: " + lastUpdate)
        
    def setRSSIIcon(self, rssi): 
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
        
    def updateSwitchIcons(self):
        keys = self.__wsc.keyEmulator.getAssignedKeys(self.__strModuleID)
        if keys[self.__wsc.keyEmulator.switchOne][1]:
            iconPath = self.__icon['switch'][0]
        else: 
            iconPath = self.__icon['switch'][1]
        
        self.__ui.buttonSwitchOne.setIcon(self.setupSwitchIcon(iconPath))
            
        if keys[self.__wsc.keyEmulator.switchTwo][1]:
            iconPath = self.__icon['switch'][2]
        else: 
            iconPath =  self.__icon['switch'][3]
        
        self.__ui.buttonSwitchTwo.setIcon(self.setupSwitchIcon(iconPath))
        
        if keys[self.__wsc.keyEmulator.switchAdaptive][1]:
            iconPath = self.__icon['switch'][4]
        else:
            iconPath = self.__icon['switch'][5]
            
        self.__ui.buttonSwitchAdaptive.setIcon(self.setupSwitchIcon(iconPath))

    def testKeys(self):
        time.sleep(3)
        for payload in [1, 0, 2, 0, 4, 0]:
            self.__wsc.keyEmulator.emulateKey(self.__strModuleID, payload)
            time.sleep(0.1)


class IdeasXMainWindow(QtWidgets.QMainWindow):
    def __init__(self, wsc):
        super(IdeasXMainWindow, self).__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__wsc = wsc 
        
        p = self.__ui.contentEncoder.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.__ui.contentEncoder.setPalette(p)
        
        self.__ui.statusMessageWidget = QtWidgets.QLabel()
        self.__ui.statusMessageWidget.setText("Starting WSC...")
        self.__ui.statusMessageWidget.setAlignment(QtCore.Qt.AlignLeft)
        self.__ui.statusbar.addWidget(self.__ui.statusMessageWidget, 1)
                
        self.__org = 'IdeasX'
        self.__app = 'Workstation-Client'
        
        self.restoreSettings()
        
        #self.__ui.buttonSettings.clicked.connect(self.updateBrokerSettings)
        self.__ui.buttonBoxNetwork.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.updateBrokerSettings)
        self.__ui.buttonBoxNetwork.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.restoreBrokerSettings)
        

    def setEncoderLayout(self, layout):
        self.__ui.contentEncoder.setLayout(layout)
        
    def setStatusBarMessage(self, msg):
        self.__ui.statusbar.clearMessage()
        self.__ui.statusMessageWidget.setText(msg)
        
    def setStatusBarUpdate(self, msg):
        self.__ui.statusbar.showMessage(msg)

    def saveSettings(self):
        '''
            Saves various backend and front information via Qt's system agnoistic classes. 
            The following information is saved and restored: 
            
            1) MainWindow size and position 
            2) Switch configuration and assigned keys 
            3) Encoder Nicknames
            4) Broker URL and Ports
        '''
        # MainWindow Settings
        settings = QtCore.QSettings(self.__org, self.__app)
        settings.beginGroup("MainWindow")
        settings.setValue("size", self.size())
        settings.setValue("pos", self.pos())
        settings.endGroup()      
        
    def updateBrokerSettings(self):
        print(self.__ui.networkBroker.text())
        self.__NetworkBroker = self.__ui.networkBroker.text()
        self.__LocalBroker = self.__ui.localBroker.text()
        self.__NetworkPort = int(self.__ui.networkPort.text())
        self.__LocalPort = int(self.__ui.localPort.text())  
        
        settings = QtCore.QSettings(self.__org, self.__app) 
        settings.beginGroup("Broker")
        settings.setValue('NetworkBroker', self.__NetworkBroker)
        settings.setValue('NetworkPort', self.__NetworkPort)
        settings.setValue('LocalBroker', self.__LocalBroker)
        settings.setValue('LocalPort', self.__LocalPort)
        settings.endGroup()
        self.saveSettings()
        
        #self.__ui.statusbar.showMessage("Updated Broker settings. Please Restart the WSC.")
        self.__wsc.guiRestartWSC()
        
    def restoreSettings(self):
        settings = QtCore.QSettings(self.__org, self.__app)
        settings.beginGroup("MainWindow")
        self.resize(settings.value("size", QtCore.QSize(525, 648)))
        self.move(settings.value("pos", QtCore.QPoint(0, 0)))
        settings.endGroup()
        
        settings.beginGroup("Broker")
        self.__NetworkBroker = settings.value('NetworkBroker', 'ideasx.duckdns.org')
        self.__NetworkPort = settings.value('NetworkPort', 1883)
        self.__LocalBroker = settings.value('LocalBroker', '10.42.0.1')
        self.__LocalPort = settings.value('LocalPort', 1883)
        settings.endGroup()
        
        self.__ui.networkBroker.setText(self.__NetworkBroker)
        self.__ui.networkPort.setText(str(self.__NetworkPort))
        self.__ui.localBroker.setText(self.__LocalBroker)
        self.__ui.localPort.setText(str(self.__LocalPort))
        
        settings.beginGroup('OTAServer')
        self.__OTAServer = settings.value('OTAServer', 'ideasx.duckdns.org')
        settings.endGroup()
        
    def restoreBrokerSettings(self):
        settings = QtCore.QSettings(self.__org, self.__app)

        settings.beginGroup("Broker")
        self.__NetworkBroker = settings.value('NetworkBroker', 'ideasx.duckdns.org')
        self.__NetworkPort = settings.value('NetworkPort', 1883)
        self.__LocalBroker = settings.value('LocalBroker', '10.42.0.1')
        self.__LocalPort = settings.value('LocalPort', 1883)
        settings.endGroup()
        
        self.__ui.networkBroker.setText(self.__NetworkBroker)
        self.__ui.networkPort.setText(str(self.__NetworkPort))
        self.__ui.localBroker.setText(self.__LocalBroker)
        self.__ui.localPort.setText(str(self.__LocalPort))
        
        
    def closeEvent(self, event):
        self.saveSettings()
        super(IdeasXMainWindow, self).closeEvent(event)
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon/logo/ideasx.png'))
    wsc = IdeasXWSCNetworkThread()
    mainWindow = IdeasXMainWindow(wsc)
    encoderManager = IdeasXDeviceManager(IdeasXEncoder, wsc)
    mainWindow.setEncoderLayout(encoderManager.returnLayout())
    
    wsc.encoderUpdate.connect(encoderManager.refreshDevices)
    wsc.networkStatus.connect(mainWindow.setStatusBarMessage)
    wsc.networkUpdate.connect(mainWindow.setStatusBarUpdate)
    #wsc.guiStartWorkstationClient('ideasx.duckdns.org')
    wsc.guiStartWorkstationClient()
    
    
    #timer = QtCore.QTimer()
    #timer.timeout.connect(mainWindow.hideEncoder)
    #timer.start(1000)
    #time.sleep(0.5)
    
    mainWindow.show()
    sys.exit(app.exec_())
    