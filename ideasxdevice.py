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
        IdeasXDevice.resize(452, 84)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IdeasXDevice.sizePolicy().hasHeightForWidth())
        IdeasXDevice.setSizePolicy(sizePolicy)
        IdeasXDevice.setMinimumSize(QtCore.QSize(452, 84))
        IdeasXDevice.setMaximumSize(QtCore.QSize(16777215, 84))
        IdeasXDevice.setAcceptDrops(False)
        IdeasXDevice.setAutoFillBackground(False)
        self.horizontalLayout = QtWidgets.QHBoxLayout(IdeasXDevice)
        self.horizontalLayout.setContentsMargins(9, 3, 9, 3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetInfo = QtWidgets.QWidget(IdeasXDevice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetInfo.sizePolicy().hasHeightForWidth())
        self.widgetInfo.setSizePolicy(sizePolicy)
        self.widgetInfo.setMinimumSize(QtCore.QSize(290, 70))
        self.widgetInfo.setObjectName("widgetInfo")
        self.labelDeviceType = QtWidgets.QLabel(self.widgetInfo)
        self.labelDeviceType.setGeometry(QtCore.QRect(5, 0, 101, 76))
        self.labelDeviceType.setToolTip("")
        self.labelDeviceType.setStatusTip("")
        self.labelDeviceType.setPixmap(QtGui.QPixmap("./icon/devicetype/modulev3b.png"))
        self.labelDeviceType.setScaledContents(False)
        self.labelDeviceType.setObjectName("labelDeviceType")
        self.labelModuleID = QtWidgets.QLabel(self.widgetInfo)
        self.labelModuleID.setGeometry(QtCore.QRect(119, 5, 311, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelModuleID.sizePolicy().hasHeightForWidth())
        self.labelModuleID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("TakaoPGothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelModuleID.setFont(font)
        self.labelModuleID.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelModuleID.setScaledContents(True)
        self.labelModuleID.setObjectName("labelModuleID")
        self.labelSignal = QtWidgets.QLabel(self.widgetInfo)
        self.labelSignal.setGeometry(QtCore.QRect(117, 43, 31, 31))
        self.labelSignal.setToolTip("")
        self.labelSignal.setPixmap(QtGui.QPixmap("./icon/network/network-wireless-signal-ok-symbolic.png"))
        self.labelSignal.setScaledContents(False)
        self.labelSignal.setObjectName("labelSignal")
        self.labelBattery = QtWidgets.QLabel(self.widgetInfo)
        self.labelBattery.setGeometry(QtCore.QRect(157, 43, 31, 31))
        self.labelBattery.setToolTip("")
        self.labelBattery.setStatusTip("")
        self.labelBattery.setPixmap(QtGui.QPixmap("./icon/battery/battery-good-charging-symbolic.png"))
        self.labelBattery.setScaledContents(False)
        self.labelBattery.setObjectName("labelBattery")
        self.buttonSwitchOne = QtWidgets.QToolButton(self.widgetInfo)
        self.buttonSwitchOne.setGeometry(QtCore.QRect(197, 43, 25, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/switch/switch-one-disabled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSwitchOne.setIcon(icon)
        self.buttonSwitchOne.setIconSize(QtCore.QSize(30, 30))
        self.buttonSwitchOne.setAutoRaise(True)
        self.buttonSwitchOne.setObjectName("buttonSwitchOne")
        self.buttonSwitchTwo = QtWidgets.QToolButton(self.widgetInfo)
        self.buttonSwitchTwo.setGeometry(QtCore.QRect(219, 43, 21, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icon/switch/switch-two-disabled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSwitchTwo.setIcon(icon1)
        self.buttonSwitchTwo.setIconSize(QtCore.QSize(30, 30))
        self.buttonSwitchTwo.setAutoRaise(True)
        self.buttonSwitchTwo.setObjectName("buttonSwitchTwo")
        self.buttonSwitchAdaptive = QtWidgets.QToolButton(self.widgetInfo)
        self.buttonSwitchAdaptive.setGeometry(QtCore.QRect(238, 43, 25, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icon/switch/switch-adaptive-disabled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSwitchAdaptive.setIcon(icon2)
        self.buttonSwitchAdaptive.setIconSize(QtCore.QSize(30, 30))
        self.buttonSwitchAdaptive.setAutoRaise(True)
        self.buttonSwitchAdaptive.setObjectName("buttonSwitchAdaptive")
        self.horizontalLayout.addWidget(self.widgetInfo)
        self.widgetControls = QtWidgets.QWidget(IdeasXDevice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetControls.sizePolicy().hasHeightForWidth())
        self.widgetControls.setSizePolicy(sizePolicy)
        self.widgetControls.setMinimumSize(QtCore.QSize(120, 66))
        self.widgetControls.setMaximumSize(QtCore.QSize(120, 66))
        self.widgetControls.setObjectName("widgetControls")
        self.labelStatus = QtWidgets.QLabel(self.widgetControls)
        self.labelStatus.setGeometry(QtCore.QRect(-70, 47, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setItalic(True)
        self.labelStatus.setFont(font)
        self.labelStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.buttonMenu = QtWidgets.QToolButton(self.widgetControls)
        self.buttonMenu.setGeometry(QtCore.QRect(95, 10, 21, 36))
        self.buttonMenu.setAutoRaise(False)
        self.buttonMenu.setArrowType(QtCore.Qt.DownArrow)
        self.buttonMenu.setObjectName("buttonMenu")
        self.buttonActivate = QtWidgets.QToolButton(self.widgetControls)
        self.buttonActivate.setGeometry(QtCore.QRect(5, 10, 91, 36))
        self.buttonActivate.setCheckable(True)
        self.buttonActivate.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.buttonActivate.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.buttonActivate.setObjectName("buttonActivate")
        self.horizontalLayout.addWidget(self.widgetControls)

        self.retranslateUi(IdeasXDevice)
        QtCore.QMetaObject.connectSlotsByName(IdeasXDevice)

    def retranslateUi(self, IdeasXDevice):
        _translate = QtCore.QCoreApplication.translate
        IdeasXDevice.setWindowTitle(_translate("IdeasXDevice", "Form"))
        self.labelModuleID.setText(_translate("IdeasXDevice", "Sarah Stanton"))
        self.buttonSwitchOne.setText(_translate("IdeasXDevice", "..."))
        self.buttonSwitchTwo.setText(_translate("IdeasXDevice", "..."))
        self.buttonSwitchAdaptive.setText(_translate("IdeasXDevice", "..."))
        self.labelStatus.setText(_translate("IdeasXDevice", "Last Update: 2:30AM"))
        self.buttonMenu.setText(_translate("IdeasXDevice", "Activate "))
        self.buttonActivate.setText(_translate("IdeasXDevice", "Activate"))

