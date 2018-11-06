# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        login.setStyleSheet("background-color:#f4f9f4;")
        self.label1 = QtWidgets.QLabel(login)
        self.label1.setGeometry(QtCore.QRect(120, 60, 131, 31))
        self.label1.setStyleSheet("border:1px groove rgb(172,172,172);\n"
"background-color:transparent;")
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.ip = QtWidgets.QLineEdit(login)
        self.ip.setGeometry(QtCore.QRect(140, 60, 91, 31))
        self.ip.setStyleSheet("background-color:transparent;\n"
"border-style:outset;")
        self.ip.setObjectName("ip")

        self.label3 = QtWidgets.QLabel(login)
        self.label3.setGeometry(QtCore.QRect(120, 100, 131, 31))
        self.label3.setStyleSheet("border:1px groove rgb(172,172,172);\n"
"background-color:transparent;")
        self.label3.setText("")
        self.label3.setObjectName("label1")
        self.username = QtWidgets.QLineEdit(login)
        self.username.setGeometry(QtCore.QRect(140, 100, 91, 31))
        self.username.setStyleSheet("background-color:transparent;\n"
"border-style:outset;")
        self.username.setObjectName("username")

        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(120, 140, 131, 31))
        self.label_2.setStyleSheet("border:1px groove rgb(172,172,172);\n"
"background-color:transparent;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pwd = QtWidgets.QLineEdit(login)
        self.pwd.setGeometry(QtCore.QRect(140, 140, 91, 31))
        self.pwd.setStyleSheet("background-color:transparent;\n"
"border-style:outset;")
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setObjectName("pwd")
        self.btn = QtWidgets.QPushButton(login)
        self.btn.setGeometry(QtCore.QRect(150, 200, 75, 23))
        self.btn.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:3px;")
        self.btn.setCheckable(True)
        self.btn.setObjectName("btn")

        self.retranslateUi(login)
        self.btn.clicked.connect(login.jump)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "结构化监测系统"))
        self.ip.setPlaceholderText(_translate("login", "请输入远程Ip"))
        self.username.setPlaceholderText(_translate("login", "请输入用户名"))
        self.pwd.setPlaceholderText(_translate("login", "请输入您的密码"))
        self.btn.setText(_translate("login", "确定"))

import img_rc
