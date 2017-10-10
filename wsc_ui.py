import logging
import sys
import time
import sip
from wsc_tools import ParsingTools
from wsc_client import WSC_Client
from wsc_device_encoder import EncoderUI

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt.mainwindow2 import Ui_MainWindow
from pyqt.ideasxdevice import Ui_IdeasXDevice
from pyqt.encoderconfigurationdialog import Ui_SwitchConfigDialog
from pyqt.devicedialog import Ui_Dialog

logging.basicConfig( level=logging.DEBUG)
log = logging.getLogger("wsc_ui") 

class UIDeviceManager():
    
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
                self.__devices[deviceMAC].updateDevice(devices[deviceMAC])
            else:
                self.__devices[deviceMAC] = self.__deviceClass(devices[deviceMAC])
                self.__deviceLayout.addWidget(self.__devices[deviceMAC])
        for deviceMAC in list(self.__devices.keys()):
            if deviceMAC not in devices.keys():
                self.removeDevice(deviceMAC)

    def removeDevice(self, deviceMAC):
        self.__deviceLayout.removeWidget(self.__devices[deviceMAC])
        sip.delete(self.__devices[deviceMAC])
        self.__devices.pop(deviceMAC)

    def returnLayout(self):
        return self.__deviceLayout

    def filterDevices(self, searchPhase):
        log.debug("This currently doesn't work")

    def printDevices(self):
        print(self.__devices)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, wsc):
        super(MainWindow, self).__init__()
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
        self.__wsc.restartWSC()

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
        super(MainWindow, self).closeEvent(event)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon/logo/ideasx.png'))
    wsc = WSC_Client()
    mainWindow = MainWindow(wsc)
    encoderManager = UIDeviceManager(EncoderUI, wsc)
    mainWindow.setEncoderLayout(encoderManager.returnLayout())

    wsc.encoderUpdate.connect(encoderManager.refreshDevices)
    wsc.networkStatus.connect(mainWindow.setStatusBarMessage)
    wsc.networkUpdate.connect(mainWindow.setStatusBarUpdate)

    wsc.StartWorkstationClient(gui=True)

    mainWindow.show()
    sys.exit(app.exec_())
