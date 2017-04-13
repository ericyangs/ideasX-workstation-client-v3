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
        SwitchConfigDialog.resize(217, 190)
        self.verticalLayout = QtWidgets.QVBoxLayout(SwitchConfigDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(SwitchConfigDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lineSwitchKey = QtWidgets.QLineEdit(self.groupBox)
        self.lineSwitchKey.setText("")
        self.lineSwitchKey.setClearButtonEnabled(True)
        self.lineSwitchKey.setObjectName("lineSwitchKey")
        self.gridLayout.addWidget(self.lineSwitchKey, 1, 0, 1, 2)
        self.labelLatch = QtWidgets.QLabel(self.groupBox)
        self.labelLatch.setObjectName("labelLatch")
        self.gridLayout.addWidget(self.labelLatch, 2, 0, 1, 1)
        self.buttonApply = QtWidgets.QPushButton(self.groupBox)
        self.buttonApply.setObjectName("buttonApply")
        self.gridLayout.addWidget(self.buttonApply, 4, 1, 1, 1)
        self.checkSwitchEnable = QtWidgets.QCheckBox(self.groupBox)
        self.checkSwitchEnable.setObjectName("checkSwitchEnable")
        self.gridLayout.addWidget(self.checkSwitchEnable, 0, 0, 1, 2)
        self.spinLatchTime = QtWidgets.QSpinBox(self.groupBox)
        self.spinLatchTime.setMaximum(60)
        self.spinLatchTime.setSingleStep(1)
        self.spinLatchTime.setObjectName("spinLatchTime")
        self.gridLayout.addWidget(self.spinLatchTime, 3, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(SwitchConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(SwitchConfigDialog)

    def retranslateUi(self, SwitchConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        SwitchConfigDialog.setWindowTitle(_translate("SwitchConfigDialog", "Dialog"))
        self.groupBox.setTitle(_translate("SwitchConfigDialog", "Switch Configuration:"))
        self.lineSwitchKey.setPlaceholderText(_translate("SwitchConfigDialog", "Enter Keystroke"))
        self.labelLatch.setText(_translate("SwitchConfigDialog", "Latching Delay:"))
        self.buttonApply.setText(_translate("SwitchConfigDialog", "Apply"))
        self.checkSwitchEnable.setText(_translate("SwitchConfigDialog", "Enable Switch"))
        self.spinLatchTime.setSuffix(_translate("SwitchConfigDialog", " seconds"))

