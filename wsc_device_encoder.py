import logging
import sys
import time 
import sip
from wsc_tools import ParsingTools
from wsc_tools import Switch
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from pyqt.ideasxdevice import Ui_IdeasXDevice
from pyqt.encoderconfigurationdialog import Ui_SwitchConfigDialog
from pyqt.devicedialog import Ui_Dialog

pt = ParsingTools()
logging.basicConfig( level=logging.DEBUG)
log = logging.getLogger("wsc_device_encoder") 

class Encoder():
    FAIL = 0
    SUCCESS = 1
    ALIVE_VALUE = b'1'
    ALIVE_TOPIC = "alive" 
    DEVICE_HEALTH_TOPIC = "encoder/+/health/#"
    DEVICE_HEALTH_QOS = 0
    SHUTDOWN_COMMAND_TOPIC = "shutdown"
    RESTART_COMMAND_TOPIC = "restart"
    OTA_COMMAND_TOPIC = "ota"
    UART_TX_COMMAND_TOPIC = "uart"
    COMMAND_RETAIN = False 
    COMMAND_QOS = 1 

    def __init__(self, device_id, mqttc):
        self.__device_id  = device_id
        self.__hw_version_default =   b"0,0"
        self.__fw_version_default =   b"0,0"
        self.__alive_default  =    b"0"
        self.__vcell_default   =   b"0"
        self.__charge_default  =   b"0"
        self.__lbi_default  =      b"0"
        self.__soc_default  =      b"0"
        self.__rom_default  =      b"0"
        self.__ota_default  =      b"0"
        self.__wireless_default  = b"0"
        self.__ssid_default    =   b""
        self.__bssid_default   =   b""
        self.__rssi_default    =   b"0"
        self.__auth_default    =   b"0"
        self.__time_default    =   time.time()
        self.__fields = {"device_id":   self.__device_id,
                         "hw_ver":      self.__hw_version_default,
                         "fw_ver":      self.__fw_version_default,
                         "alive":       self.__alive_default,
                         "vcell":       self.__vcell_default,
                         "charge":      self.__charge_default,
                         "lbi":         self.__lbi_default,
                         "soc":         self.__soc_default,
                         "rom":         self.__rom_default,
                         "ota":         self.__ota_default,
                         "wireless":    self.__wireless_default,
                         "ssid":        self.__ssid_default,
                         "bssid":       self.__bssid_default,
                         "rssi":        self.__rssi_default,
                         "auth":        self.__auth_default,
                         "time":        self.__time_default}
        self.__commands = {'update':    self.update,
                           'restart':   self.restart,
                           'shutdown':  self.shutdown}
        self.__mqttc = mqttc
        self.switchOne = Switch()
        self.switchTwo = Switch()
        self.switchAdaptive = Switch()
        self.RAW_COMMAND_TOPIC = "encoder/" + device_id + "/command/"


    def updateField(self, field, value):
        if field in self.__fields.keys():
            self.__fields[field] = value
            self.__fields['time'] = time.time()
            return Encoder.SUCCESS
        else: 
            return Encoder.FAIL
        
    def listFieldNames(self):
        return self.__fields.keys()
        
    def listFields(self):
        return self.__fields

    def listCommandNames(self):
        return self.__commands.keys() 

    def listCommands(self):
        return self.__commmands
    
    def getField(self, field):
        return self.__fields[field]

    def update(self): 
        self.__mqttc.publish(self.RAW_COMMAND_TOPIC+self.OTA_COMMAND_TOPIC, b'1', qos=1, retain=False)
        log.info("sent OTA command")

    def restart(self):
        self.__mqttc.publish(self.RAW_COMMAND_TOPIC+self.RESTART_COMMAND_TOPIC, b'1', qos=1, retain=False)
        log.info("sent restart command")  

    def shutdown(self): 
        self.__mqttc.publish(self.RAW_COMMAND_TOPIC+self.SHUTDOWN_COMMAND_TOPIC, b'1', qos=1, retain=False)
        log.info("sent shutdown command")  

class EncoderUI(QtWidgets.QWidget):
    sendCommand = QtCore.pyqtSignal(['QString'], name='sendCommand')
    activateDevice = QtCore.pyqtSignal(['QString', 'QString'], name='deactivateDevice')
    deactivateDevice = QtCore.pyqtSignal(['QString', 'QString'], name='activateDevice')
    __pathToIcon = {'network': './icon/network/',
                     'battery': './icon/battery/',
                     'battery_charging': './icon/battery/',
                     'switch': './icon/switch/'
                    }
    __icon =    {'network':   ['network-wireless-offline-symbolic.png',
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
    __deviceType = 'encoder/'


    def __init__(self, encoder):
        self.__deviceName = None
        self.__encoder = encoder

        # Setup UI components
        super(EncoderUI, self).__init__()
        self.__ui = Ui_IdeasXDevice()
        self.__ui.setupUi(self)
        self.updateDevice(encoder)
        self.updateSwitchIcons()

        # Setup Signals
        self.setupMenu()
        #self.__ui.buttonActivate.clicked.connect(self.activateEncoder)
        self.__ui.buttonSwitchOne.clicked.connect(lambda: self.openSwitchDialog(self.__encoder.switchOne))
        self.__ui.buttonSwitchTwo.clicked.connect(lambda: self.openSwitchDialog(self.__encoder.switchTwo))
        #self.activateDevice.connect(self.__wsc.activateEncoder)
        #self.deactivateDevice.connect(self.__wsc.deactivateEncoder)

    def openDeviceInformation(self):
        dialog = InfoUI()
        dialog.updateDisplay(self.__encoder.listFields())
        dialog.newDeviceName.connect(self.setDeviceAlisas)
        dialog.exec()

    def openSwitchDialog(self, switch):
        dialog = SwitchUI(switch)
        if dialog.exec_():
            if dialog.key != None and len(dialog.key) == 1:
                switch.setConfig(dialog.key, latch=False,interval=0.0, release=False, enable=dialog.enable)
                self.updateSwitchIcons()

    def setupSwitchIcon(self, path):
        icon = QtGui.QIcon()
        iconPath = self.__pathToIcon['switch']
        iconPath = iconPath + path
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def setupMenu(self):

        # create menu actions 
        shutdownAction = QtWidgets.QAction('Shutdown', self)
        resetAction = QtWidgets.QAction("Reset", self)
        testKeysAction = QtWidgets.QAction("Test Keys", self)
        openInfoAction = QtWidgets.QAction("Information", self)
        startOTAAction = QtWidgets.QAction("OTA Update", self)

        # connect signals to funcitons 
        #testKeysAction.triggered.connect(self.testKeys)
        openInfoAction.triggered.connect(self.openDeviceInformation)
        startOTAAction.triggered.connect(lambda: self.__encoder.update())
        shutdownAction.triggered.connect(lambda: self.__encoder.shutdown())
        resetAction.triggered.connect(lambda: self.__encoder.restart())

        # create menu options 
        deviceMenu = QtWidgets.QMenu()
        deviceMenu.addAction(shutdownAction)
        deviceMenu.addAction(resetAction)
        deviceMenu.addAction(openInfoAction)
        deviceMenu.addSection("Engineering Tools")
        #deviceMenu.addAction(testKeysAction)
        #deviceMenu.addAction(startOTAAction)

        self.__ui.buttonMenu.setPopupMode(2)
        self.__ui.buttonMenu.setMenu(deviceMenu)
        self.__ui.buttonMenu.setStyleSheet("* { padding-right: 3px } QToolButton::menu-indicator { image: none }")

    def activateEncoder(self):
        if self.__ui.buttonActivate.text() == "Activate":
            log.info("Activating Encoder: " + self.__ui.labelModuleID.text())
            self.activateDevice.emit(self.__strModuleID, self.__deviceType)
            self.__ui.buttonActivate.setText("Deactivate")
        else:
            log.info("Deactivating Encoder: " + self.__ui.labelModuleID.text())
            self.deactivateDevice.emit(self.__strModuleID, self.__deviceType)
            self.__ui.buttonActivate.setText("Activate")

    def updateDevice(self, encoder):
        self.__encoder = encoder
        self.__rssi = encoder.getField('rssi')
        self.__soc = pt.calculateSOC(encoder.getField('soc'))
        self.__vcell = pt.calculateVCell(encoder.getField('vcell'))
        self.__strModuleID = encoder.getField('device_id')
        self.__updateTime = encoder.getField('time')
        self.__ota = encoder.getField('ota')

        if self.__deviceName == None:
            self.setModuleID(self.__strModuleID)
        self.setSOCIcon(self.__soc)
        self.setRSSIIcon(self.__rssi)
        self.setStatusTime(self.__updateTime)
        self.setOTAIcon(self.__ota)

    def setOTAIcon(self, ota):
        if ota == '1':
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
        soc = int(soc)
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
        rssi = int(rssi)
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
        switch1 = self.__encoder.switchOne
        switch2 = self.__encoder.switchTwo
        switchA = self.__encoder.switchAdaptive
        switchA.deactivate()

        if switch1.active:
            iconPath = self.__icon['switch'][0]
        else:
            iconPath = self.__icon['switch'][1]

        self.__ui.buttonSwitchOne.setIcon(self.setupSwitchIcon(iconPath))

        if switch2.active:
            iconPath = self.__icon['switch'][2]
        else:
            iconPath =  self.__icon['switch'][3]

        self.__ui.buttonSwitchTwo.setIcon(self.setupSwitchIcon(iconPath))

        if switchA.active: 
            iconPath = self.__icon['switch'][4]
        else:
            iconPath = self.__icon['switch'][5]

        self.__ui.buttonSwitchAdaptive.setIcon(self.setupSwitchIcon(iconPath))

    def testKeys(self):
        time.sleep(3)
        for payload in [1, 0, 2, 0, 4, 0]:
            self.__wsc.keyEmulator.emulateKey(self.__strModuleID, payload)
            time.sleep(0.1)

class SwitchUI(QtWidgets.QDialog):

    def __init__(self, switch):
        super(SwitchUI, self).__init__()
        self.__ui = Ui_SwitchConfigDialog()
        self.__ui.setupUi(self)
        self.__ui.buttonApply.clicked.connect(self.submitOnClose)
        self.key = switch.getKey()
        self.enable = switch.getActive()
        self.switch = switch

        self.__ui.checkSwitchEnable.setChecked(self.enable)
        self.__ui.lineSwitchKey.setText(self.key)

    def submitOnClose(self):
        self.key = self.__ui.lineSwitchKey.text()
        self.enable = self.__ui.checkSwitchEnable.isChecked()
        self.accept()

class InfoUI(QtWidgets.QDialog):
    newDeviceName = QtCore.pyqtSignal(['QString'], name='newDeviceName')

    def __init__(self):
        super(InfoUI, self).__init__()
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)
        self.__ui.lineAlias.textEdited.connect(lambda: self.newDeviceName.emit(self.__ui.lineAlias.text()))

    def updateDisplay(self, encoder):
        self.__ui.labelBatteryCapacity.setText(encoder['soc'].decode('utf-8'))
        self.__ui.labelBatteryVoltage.setText(str(encoder['vcell'].decode('utf-8')))
        self.__ui.labelLowBattery.setText(str(encoder['lbi'].decode('utf-8')))
        self.__ui.labelChargeState.setText('N/A')

        self.__ui.labelActiveFlag.setText('N/A')
        self.__ui.labelAliveFlag.setText(str(encoder['alive'].decode('utf-8')))
        self.__ui.labelFirmwareVersion.setText(str(encoder['fw_ver'].decode('utf-8')))
        self.__ui.labelHardwareVersion.setText(str(encoder['hw_ver'].decode('utf-8')))
        self.__ui.labelOTAFlag.setText(str(encoder['ota'].decode('utf-8')))
        self.__ui.labelROMSlot.setText(str(encoder['rom'].decode('utf-8')))

        self.__ui.labelMAC.setText(str(encoder['device_id']))
        self.__ui.labelRSSI.setText(str(encoder['rssi'].decode('utf-8')))
        self.__ui.labelSSID.setText(str(encoder['ssid'].decode('utf-8')))

if __name__ == "__main__":
    deviceID = '23:45:21:23:32'

    
    encoder = Encoder(deviceID, None)
    print(pt.calculateSOC(encoder.getField('soc')))
    app = QtWidgets.QApplication(sys.argv)
    encoderUI = EncoderUI(encoder)
    
    encoderUI.show() 
    sys.exit(app.exec_())
