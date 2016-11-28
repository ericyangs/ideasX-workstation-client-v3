# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 648)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.VerticalTabs)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabEncoder = QtWidgets.QWidget()
        self.tabEncoder.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabEncoder.setObjectName("tabEncoder")
        self.gridLayout = QtWidgets.QGridLayout(self.tabEncoder)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName("gridLayout")
        self.searchEncoder = QtWidgets.QLineEdit(self.tabEncoder)
        self.searchEncoder.setClearButtonEnabled(True)
        self.searchEncoder.setObjectName("searchEncoder")
        self.gridLayout.addWidget(self.searchEncoder, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.scrollEncoder = QtWidgets.QScrollArea(self.tabEncoder)
        self.scrollEncoder.setAutoFillBackground(False)
        self.scrollEncoder.setStyleSheet("")
        self.scrollEncoder.setWidgetResizable(True)
        self.scrollEncoder.setObjectName("scrollEncoder")
        self.contentEncoder = QtWidgets.QWidget()
        self.contentEncoder.setGeometry(QtCore.QRect(0, 0, 459, 556))
        self.contentEncoder.setObjectName("contentEncoder")
        self.scrollEncoder.setWidget(self.contentEncoder)
        self.gridLayout.addWidget(self.scrollEncoder, 0, 0, 1, 3)
        self.tabWidget.addTab(self.tabEncoder, "")
        self.tabActuator = QtWidgets.QWidget()
        self.tabActuator.setObjectName("tabActuator")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabActuator)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.searchActuator = QtWidgets.QLineEdit(self.tabActuator)
        self.searchActuator.setAutoFillBackground(False)
        self.searchActuator.setFrame(True)
        self.searchActuator.setClearButtonEnabled(True)
        self.searchActuator.setObjectName("searchActuator")
        self.gridLayout_2.addWidget(self.searchActuator, 1, 1, 1, 1)
        self.tableActuator = QtWidgets.QTableView(self.tabActuator)
        self.tableActuator.setEnabled(True)
        self.tableActuator.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableActuator.setAlternatingRowColors(True)
        self.tableActuator.setShowGrid(False)
        self.tableActuator.setSortingEnabled(True)
        self.tableActuator.setObjectName("tableActuator")
        self.tableActuator.horizontalHeader().setStretchLastSection(True)
        self.tableActuator.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableActuator, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tabActuator, "")
        self.tabSetting = QtWidgets.QWidget()
        self.tabSetting.setObjectName("tabSetting")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabSetting)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupNetwork = QtWidgets.QGroupBox(self.tabSetting)
        self.groupNetwork.setObjectName("groupNetwork")
        self.formLayout = QtWidgets.QFormLayout(self.groupNetwork)
        self.formLayout.setObjectName("formLayout")
        self.labelNetworkBroker = QtWidgets.QLabel(self.groupNetwork)
        self.labelNetworkBroker.setObjectName("labelNetworkBroker")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelNetworkBroker)
        self.networkBroker = QtWidgets.QLineEdit(self.groupNetwork)
        self.networkBroker.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.networkBroker.setObjectName("networkBroker")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.networkBroker)
        self.networkPort = QtWidgets.QLineEdit(self.groupNetwork)
        self.networkPort.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.networkPort.setText("")
        self.networkPort.setObjectName("networkPort")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.networkPort)
        self.labelLocalBroker = QtWidgets.QLabel(self.groupNetwork)
        self.labelLocalBroker.setObjectName("labelLocalBroker")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelLocalBroker)
        self.localBroker = QtWidgets.QLineEdit(self.groupNetwork)
        self.localBroker.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.localBroker.setObjectName("localBroker")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.localBroker)
        self.localPort = QtWidgets.QLineEdit(self.groupNetwork)
        self.localPort.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.localPort.setObjectName("localPort")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.localPort)
        self.otaServer = QtWidgets.QLineEdit(self.groupNetwork)
        self.otaServer.setText("")
        self.otaServer.setObjectName("otaServer")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.otaServer)
        self.labelOTA = QtWidgets.QLabel(self.groupNetwork)
        self.labelOTA.setObjectName("labelOTA")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelOTA)
        self.verticalLayout_2.addWidget(self.groupNetwork)
        self.buttonBoxNetwork = QtWidgets.QDialogButtonBox(self.tabSetting)
        self.buttonBoxNetwork.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBoxNetwork.setObjectName("buttonBoxNetwork")
        self.verticalLayout_2.addWidget(self.buttonBoxNetwork)
        self.groupDeviceSettings = QtWidgets.QGroupBox(self.tabSetting)
        self.groupDeviceSettings.setObjectName("groupDeviceSettings")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupDeviceSettings)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelAPSelector = QtWidgets.QLabel(self.groupDeviceSettings)
        self.labelAPSelector.setObjectName("labelAPSelector")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelAPSelector)
        self.selectAP = QtWidgets.QSpinBox(self.groupDeviceSettings)
        self.selectAP.setSuffix("")
        self.selectAP.setMinimum(1)
        self.selectAP.setMaximum(5)
        self.selectAP.setObjectName("selectAP")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.selectAP)
        self.labelSSID = QtWidgets.QLabel(self.groupDeviceSettings)
        self.labelSSID.setObjectName("labelSSID")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelSSID)
        self.wifiSSID = QtWidgets.QLineEdit(self.groupDeviceSettings)
        self.wifiSSID.setObjectName("wifiSSID")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.wifiSSID)
        self.labelPassword = QtWidgets.QLabel(self.groupDeviceSettings)
        self.labelPassword.setObjectName("labelPassword")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.wifiPassword = QtWidgets.QLineEdit(self.groupDeviceSettings)
        self.wifiPassword.setObjectName("wifiPassword")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.wifiPassword)
        self.verticalLayout_2.addWidget(self.groupDeviceSettings, 0, QtCore.Qt.AlignTop)
        self.buttonBoxDevice = QtWidgets.QDialogButtonBox(self.tabSetting)
        self.buttonBoxDevice.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBoxDevice.setObjectName("buttonBoxDevice")
        self.verticalLayout_2.addWidget(self.buttonBoxDevice)
        self.groupUpdat = QtWidgets.QGroupBox(self.tabSetting)
        self.groupUpdat.setObjectName("groupUpdat")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupUpdat)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupUpdat)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupUpdat)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.label = QtWidgets.QLabel(self.groupUpdat)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout_2.addWidget(self.groupUpdat)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabSetting)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.tabWidget.addTab(self.tabSetting, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setToolTipDuration(-7)
        self.statusbar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IdeasX Workstation Client"))
        self.searchEncoder.setPlaceholderText(_translate("MainWindow", "Search for Encoders..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEncoder), _translate("MainWindow", "Encoders"))
        self.searchActuator.setPlaceholderText(_translate("MainWindow", "Search for Actuator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabActuator), _translate("MainWindow", "Actuators"))
        self.groupNetwork.setTitle(_translate("MainWindow", "Network Settings"))
        self.labelNetworkBroker.setText(_translate("MainWindow", "Network Broker:"))
        self.networkBroker.setPlaceholderText(_translate("MainWindow", "URL or IP"))
        self.networkPort.setPlaceholderText(_translate("MainWindow", "Port"))
        self.labelLocalBroker.setText(_translate("MainWindow", "Local Broker:"))
        self.localBroker.setPlaceholderText(_translate("MainWindow", "URL or IP"))
        self.localPort.setPlaceholderText(_translate("MainWindow", "Port"))
        self.otaServer.setPlaceholderText(_translate("MainWindow", "URL or IP"))
        self.labelOTA.setText(_translate("MainWindow", "OTA Server:"))
        self.groupDeviceSettings.setTitle(_translate("MainWindow", "Device Settings"))
        self.labelAPSelector.setText(_translate("MainWindow", "Wi-Fi Access Point:"))
        self.selectAP.setPrefix(_translate("MainWindow", "Access Point "))
        self.labelSSID.setText(_translate("MainWindow", "SSID:"))
        self.labelPassword.setText(_translate("MainWindow", "Password:"))
        self.groupUpdat.setTitle(_translate("MainWindow", "WSC Update Settings"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "URL to GitHub Repository"))
        self.pushButton.setText(_translate("MainWindow", "Check for Update"))
        self.label.setText(_translate("MainWindow", "WSC Software Repository:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Global Commands"))
        self.label_2.setText(_translate("MainWindow", "Global Command: "))
        self.pushButton_2.setText(_translate("MainWindow", "Send Command"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetting), _translate("MainWindow", "Settings"))

