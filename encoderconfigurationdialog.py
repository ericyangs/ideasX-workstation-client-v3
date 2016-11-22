# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encoderconfigurationdialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SwitchConfigDialog(object):
    def setupUi(self, SwitchConfigDialog):
        SwitchConfigDialog.setObjectName("SwitchConfigDialog")
        SwitchConfigDialog.resize(217, 110)
        self.verticalLayout = QtWidgets.QVBoxLayout(SwitchConfigDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(SwitchConfigDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.checkSwitchEnable = QtWidgets.QCheckBox(self.groupBox)
        self.checkSwitchEnable.setObjectName("checkSwitchEnable")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkSwitchEnable)
        self.spinLatchTime = QtWidgets.QSpinBox(self.groupBox)
        self.spinLatchTime.setObjectName("spinLatchTime")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinLatchTime)
        self.lineSwitchKey = QtWidgets.QLineEdit(self.groupBox)
        self.lineSwitchKey.setText("")
        self.lineSwitchKey.setClearButtonEnabled(True)
        self.lineSwitchKey.setObjectName("lineSwitchKey")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineSwitchKey)
        self.labelLatch = QtWidgets.QLabel(self.groupBox)
        self.labelLatch.setObjectName("labelLatch")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelLatch)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(SwitchConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(SwitchConfigDialog)

    def retranslateUi(self, SwitchConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        SwitchConfigDialog.setWindowTitle(_translate("SwitchConfigDialog", "Dialog"))
        self.groupBox.setTitle(_translate("SwitchConfigDialog", "Switch Configuration:"))
        self.checkSwitchEnable.setText(_translate("SwitchConfigDialog", "Enable"))
        self.spinLatchTime.setSuffix(_translate("SwitchConfigDialog", " sec."))
        self.lineSwitchKey.setPlaceholderText(_translate("SwitchConfigDialog", "Enter Keystroke"))
        self.labelLatch.setText(_translate("SwitchConfigDialog", "Latching Delay:"))

