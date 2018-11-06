# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resourceManage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(601, 540)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 10, 131, 21))
        self.label.setObjectName("label")
        self.mem = QtWidgets.QTextBrowser(Form)
        self.mem.setGeometry(QtCore.QRect(0, 30, 581, 101))
        self.mem.setObjectName("mem")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 161, 16))
        self.label_2.setObjectName("label_2")
        self.hard = QtWidgets.QTextBrowser(Form)
        self.hard.setGeometry(QtCore.QRect(0, 160, 581, 111))
        self.hard.setObjectName("hard")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "内存   单位：M"))
        self.label_2.setText(_translate("Form", "硬盘   单位:M"))

