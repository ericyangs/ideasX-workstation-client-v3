# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devicedialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(357, 428)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.IdInfo = QtWidgets.QGroupBox(Dialog)
        self.IdInfo.setObjectName("IdInfo")
        self.formLayout = QtWidgets.QFormLayout(self.IdInfo)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.IdInfo)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineAlias = QtWidgets.QLineEdit(self.IdInfo)
        self.lineAlias.setObjectName("lineAlias")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineAlias)
        self.label_2 = QtWidgets.QLabel(self.IdInfo)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.labelMAC = QtWidgets.QLabel(self.IdInfo)
        self.labelMAC.setObjectName("labelMAC")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelMAC)
        self.label_24 = QtWidgets.QLabel(self.IdInfo)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.labelSSID = QtWidgets.QLabel(self.IdInfo)
        self.labelSSID.setObjectName("labelSSID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelSSID)
        self.label_26 = QtWidgets.QLabel(self.IdInfo)
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.labelRSSI = QtWidgets.QLabel(self.IdInfo)
        self.labelRSSI.setObjectName("labelRSSI")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelRSSI)
        self.verticalLayout.addWidget(self.IdInfo, 0, QtCore.Qt.AlignTop)
        self.HWSpecsAndStatus = QtWidgets.QGroupBox(Dialog)
        self.HWSpecsAndStatus.setObjectName("HWSpecsAndStatus")
        self.formLayout_3 = QtWidgets.QFormLayout(self.HWSpecsAndStatus)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_12 = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.labelFirmwareVersion = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.labelFirmwareVersion.setObjectName("labelFirmwareVersion")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelFirmwareVersion)
        self.labelHardwareVersion = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.labelHardwareVersion.setObjectName("labelHardwareVersion")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelHardwareVersion)
        self.labelROMSlot = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.labelROMSlot.setObjectName("labelROMSlot")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelROMSlot)
        self.label_18 = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.labelAliveFlag = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.labelAliveFlag.setObjectName("labelAliveFlag")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelAliveFlag)
        self.label_20 = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.labelActiveFlag = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.labelActiveFlag.setObjectName("labelActiveFlag")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.labelActiveFlag)
        self.label_22 = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.label_22.setObjectName("label_22")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.labelOTAFlag = QtWidgets.QLabel(self.HWSpecsAndStatus)
        self.labelOTAFlag.setObjectName("labelOTAFlag")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.labelOTAFlag)
        self.verticalLayout.addWidget(self.HWSpecsAndStatus, 0, QtCore.Qt.AlignTop)
        self.BatteryInfo = QtWidgets.QGroupBox(Dialog)
        self.BatteryInfo.setObjectName("BatteryInfo")
        self.formLayout_2 = QtWidgets.QFormLayout(self.BatteryInfo)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.BatteryInfo)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.labelBatteryVoltage = QtWidgets.QLabel(self.BatteryInfo)
        self.labelBatteryVoltage.setObjectName("labelBatteryVoltage")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelBatteryVoltage)
        self.label_6 = QtWidgets.QLabel(self.BatteryInfo)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.labelBatteryCapacity = QtWidgets.QLabel(self.BatteryInfo)
        self.labelBatteryCapacity.setObjectName("labelBatteryCapacity")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelBatteryCapacity)
        self.label_10 = QtWidgets.QLabel(self.BatteryInfo)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.labelChargeState = QtWidgets.QLabel(self.BatteryInfo)
        self.labelChargeState.setObjectName("labelChargeState")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelChargeState)
        self.label_16 = QtWidgets.QLabel(self.BatteryInfo)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.labelLowBattery = QtWidgets.QLabel(self.BatteryInfo)
        self.labelLowBattery.setObjectName("labelLowBattery")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelLowBattery)
        self.verticalLayout.addWidget(self.BatteryInfo, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.IdInfo.setTitle(_translate("Dialog", "Identifcation Information"))
        self.label.setText(_translate("Dialog", "Device Alias:"))
        self.label_2.setText(_translate("Dialog", "Device MAC Address:"))
        self.labelMAC.setText(_translate("Dialog", "TextLabel"))
        self.label_24.setText(_translate("Dialog", "AP SSID: "))
        self.labelSSID.setText(_translate("Dialog", "TextLabel"))
        self.label_26.setText(_translate("Dialog", "RSSI (dBm):"))
        self.labelRSSI.setText(_translate("Dialog", "TextLabel"))
        self.HWSpecsAndStatus.setTitle(_translate("Dialog", "Hardware Specifications and Status"))
        self.label_8.setText(_translate("Dialog", "Firmware Version:"))
        self.label_9.setText(_translate("Dialog", "Hardware Version:"))
        self.label_12.setText(_translate("Dialog", "ROM Slot:"))
        self.labelFirmwareVersion.setText(_translate("Dialog", "TextLabel"))
        self.labelHardwareVersion.setText(_translate("Dialog", "TextLabel"))
        self.labelROMSlot.setText(_translate("Dialog", "TextLabel"))
        self.label_18.setText(_translate("Dialog", "Alive Flag:"))
        self.labelAliveFlag.setText(_translate("Dialog", "TextLabel"))
        self.label_20.setText(_translate("Dialog", "Active Flag:"))
        self.labelActiveFlag.setText(_translate("Dialog", "TextLabel"))
        self.label_22.setText(_translate("Dialog", "OTA Flag:"))
        self.labelOTAFlag.setText(_translate("Dialog", "TextLabel"))
        self.BatteryInfo.setTitle(_translate("Dialog", "Battery Information"))
        self.label_4.setText(_translate("Dialog", "Voltage (V):"))
        self.labelBatteryVoltage.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "Remaining Capacity:"))
        self.labelBatteryCapacity.setText(_translate("Dialog", "TextLabel"))
        self.label_10.setText(_translate("Dialog", "Charging State:"))
        self.labelChargeState.setText(_translate("Dialog", "TextLabel"))
        self.label_16.setText(_translate("Dialog", "Low Battery Indicator:"))
        self.labelLowBattery.setText(_translate("Dialog", "TextLabel"))

