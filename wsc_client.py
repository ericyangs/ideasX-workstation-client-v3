import sys, time, collections
from PyQt5.QtCore import QObject, pyqtSignal, QSettings, QTimer
import paho.mqtt.client as mqtt
import logging
import wsc_device
import wsc_device_encoder
from wsc_tools import ParsingTools, EncoderConfig

#FORMAT = '%(asctime)-15s'
logging.basicConfig( level=logging.DEBUG)
log = logging.getLogger("wsc_client") 


class WSC_Client(QObject):

    # define Qt signals (I don't understand why this is here)
    encoderUpdate = pyqtSignal([dict], name='encoderUpdate')
    networkStatus = pyqtSignal([str], name='networkStatus')
    networkUpdate = pyqtSignal([str], name='networkUpdate')
    settingsError = pyqtSignal([str], name='settingsError')

    def __init__(self, settingFile=None, clientID = None, debug=True, mqttdebug=True):
        super(WSC_Client, self).__init__()
        # Private Class Flags and Variables
        self.__clientID = clientID
        self.__settingFile = settingFile
        self.__debug = debug
        self.__mqttDebug = mqttdebug
        self.__errorIndex = 0
        self.__refreshCb = None

        self.__org = 'IdeasX'
        self.__app = 'Workstation-Client'

        # MQTT Client Object
        self._mqttc = mqtt.Client(self.__clientID, clean_session=True, userdata=None, protocol=mqtt.MQTTv311)

        # IdeasX Device Managers / Parsers 
        self.__encoderManager = wsc_device.DeviceManager(wsc_device_encoder.Encoder, self._mqttc, self.encoderUpdate)
        self.__parserTools = ParsingTools()

        self._mqttc.on_connect = self.wsc_on_connect
        self._mqttc.on_disconnect = self.wsc_on_disconnect
        self.encoderConfig = EncoderConfig()

        if self.__mqttDebug:
            self._mqttc.on_log = self.mqtt_on_log

    '''
     MQTT Callback Functions
    '''

    def wsc_on_connect(self, mqttc, backend_data, flags, rc):
        if rc == 0:
            log.info('Connected to %s: %s' % (mqttc._host, mqttc._port))
            self.networkStatus.emit("Connected to %s: %s" % (mqttc._host, mqttc._port))
        else:
            log.info('rc: ' + str(rc))
            self.networkStatus.emit('Connection Failure (rc: ' +str(rc))

    def wsc_on_disconnect(self, mqttc, backend_data, rc):
        if self.__debug:
            if rc != 0:
                log.warning("Client disconnected and its a mystery why!")
                self.networkStatus.emit("Uh No! WSC was disconnected!")
            else:
                log.info("Client successfully disconnected.")
                self.networkStatus.emit("Uh No! WSC was disconnected!")
            self.printLine()

    def mqtt_on_log(self, mqttc, backend_data, level, string):
        log.debug(string)


    def StartWorkstationClient(self, ip=None, port=1883, keepAlive=60, gui=False):
        self.keepAlive = keepAlive

        if ip == None or ip == "":
            settings = QSettings(self.__org, self.__app)
            settings.beginGroup('Broker')
            self.ip = settings.value('NetworkBroker', 'ideasx.duckdns.org')
            self.port = settings.value('NetworkPort', 1883)
            self.__LocalBroker = settings.value('LocalBroker', '10.42.0.1')
            self.__LocalPort = settings.value('LocalPort', 1883)
            settings.endGroup()
        else:
            log.info("Loading hardcoded defaults")
            self.ip = ip
            self.port = port

        try:
            self._mqttc.reconnect_delay_set(1,120)
            self._mqttc.connect(self.ip, int(self.port), self.keepAlive)
            self.__encoderManager.setupMQTT()
            if gui: 
                log.info("Starting WSC Backend (GUI Version)")
                self._mqttc.loop_start()    # start MQTT Client Thread
            else: 
                log.info("Starting WSC Backend (CMD Version)")
                self._mqttc.loop_forever()  # needs to be blocking in CMD mode
        except Exception as e:
            # this needs to be updated to look at the exception errors 
             log.critical("Error connecting to IdeasX")
             log.critical(e)   
             self.networkStatus.emit("Oh-no! Broker settings are incorrect or there is a network failure")
             #sys.exit(1)

    def connectionTimeout(self):
        self.killWSC() 
        self.networkUpdate.emit("Oh-no! Broker settings are incorrect or there is a network failure")
        log.info("connection timeout")

    def restartWSC(self):
        self.killWSC()
        self.networkUpdate.emit("Restarting WSC...")
        self.StartWorkstationClient()

    def killWSC(self):
        self._mqttc.loop_stop()
        log.info("Murdered MQTT thread.")

    def printLine(self):
        print('-'*70)

if __name__ == "__main__":
    Host = "127.0.0.1"
    Port = 1883
    KeepAlive = 30
    msgFlag = False;
    deviceID = None;
    cmdPayload = None;
    cmdArg = None;
    cmdTest = True;

    wsc = WSC_Client()

    if cmdTest:
        wsc.StartWorkstationClient(Host, Port, KeepAlive, gui=False)
    else:
        wsc.StartWorkstationClient(Host, Port, KeepAlive, gui=True)
        time.sleep(3)

        (result, mid) = wsc._mqttc.subscribe('/encoders/18:fe:34:d2:6f:68/health', qos=0)
        print(result, mid)
        (result, mid) = wsc._mqttc.subscribe('/encoders/18:fe:34:d2:6f:68/health', qos=0)
        print(result, mid)
        wsc.activateEncoder('18:fe:34:d2:6f:68')
#         print(wsc.subscribedEncoders)
#         time.sleep(2)
#         wsc.deactivateEncoder('18:fe:34:d2:6f:68')
#         print(wsc.subscribedEncoders)
        time.sleep(10)
        wsc.killWSC()
