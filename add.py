# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/add.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Add_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(385, 67)
        Form.setMinimumSize(QtCore.QSize(385, 67))
        Form.setMaximumSize(QtCore.QSize(385, 67))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton2 = QtWidgets.QRadioButton(Form)
        self.radioButton2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.radioButton2.setChecked(False)
        self.radioButton2.setObjectName("radioButton2")
        self.gridLayout.addWidget(self.radioButton2, 1, 0, 1, 1)
        self.radioButton1 = QtWidgets.QRadioButton(Form)
        self.radioButton1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.radioButton1.setChecked(True)
        self.radioButton1.setObjectName("radioButton1")
        self.gridLayout.addWidget(self.radioButton1, 0, 0, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 1, 3, 1, 1)
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить"))
        self.radioButton2.setText(_translate("Form", "Варианты"))
        self.radioButton1.setText(_translate("Form", "Студенты"))
        self.cancelButton.setText(_translate("Form", "Отмена"))
        self.okButton.setText(_translate("Form", "ОК"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Введите данные"))