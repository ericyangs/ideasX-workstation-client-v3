# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ideasxdevice.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IdeasXDevice(object):
    def setupUi(self, IdeasXDevice):
        IdeasXDevice.setObjectName("IdeasXDevice")
        IdeasXDevice.resize(416, 70)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IdeasXDevice.sizePolicy().hasHeightForWidth())
        IdeasXDevice.setSizePolicy(sizePolicy)
        IdeasXDevice.setMinimumSize(QtCore.QSize(416, 70))
        IdeasXDevice.setAutoFillBackground(False)
        self.buttonActivate = QtWidgets.QPushButton(IdeasXDevice)
        self.buttonActivate.setGeometry(QtCore.QRect(289, 11, 121, 31))
        self.buttonActivate.setAutoFillBackground(False)
        self.buttonActivate.setCheckable(True)
        self.buttonActivate.setChecked(False)
        self.buttonActivate.setObjectName("buttonActivate")
        self.labelModuleID = QtWidgets.QLabel(IdeasXDevice)
        self.labelModuleID.setGeometry(QtCore.QRect(110, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(20)
        font.setItalic(False)
        self.labelModuleID.setFont(font)
        self.labelModuleID.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelModuleID.setObjectName("labelModuleID")
        self.labelStatus = QtWidgets.QLabel(IdeasXDevice)
        self.labelStatus.setGeometry(QtCore.QRect(280, 50, 127, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(6)
        font.setItalic(True)
        self.labelStatus.setFont(font)
        self.labelStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.labelBattery = QtWidgets.QLabel(IdeasXDevice)
        self.labelBattery.setGeometry(QtCore.QRect(110, 40, 91, 16))
        self.labelBattery.setObjectName("labelBattery")
        self.labelRSSI = QtWidgets.QLabel(IdeasXDevice)
        self.labelRSSI.setGeometry(QtCore.QRect(110, 50, 91, 16))
        self.labelRSSI.setObjectName("labelRSSI")
        self.label = QtWidgets.QLabel(IdeasXDevice)
        self.label.setGeometry(QtCore.QRect(10, 0, 91, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon/devicetype/modulev3.png"))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(IdeasXDevice)
        self.line.setGeometry(QtCore.QRect(-13, 60, 431, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(IdeasXDevice)
        QtCore.QMetaObject.connectSlotsByName(IdeasXDevice)

    def retranslateUi(self, IdeasXDevice):
        _translate = QtCore.QCoreApplication.translate
        IdeasXDevice.setWindowTitle(_translate("IdeasXDevice", "Form"))
        self.buttonActivate.setText(_translate("IdeasXDevice", "Activate"))
        self.labelModuleID.setText(_translate("IdeasXDevice", "2f:32:56:4f:72"))
        self.labelStatus.setText(_translate("IdeasXDevice", "Last Update: 7:46AM"))
        self.labelBattery.setText(_translate("IdeasXDevice", "Battery:  98%"))
        self.labelRSSI.setText(_translate("IdeasXDevice", "RSSI:  -54dBm"))

