# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
#删除员工信息
class rightDock(QtWidgets.QWidget):
    def __init__(self):
        super(rightDock, self).__init__()
        content = self.parent()
        #print(content)
        #停靠窗口1
        self.dock1=QDockWidget(self.tr("系统状态"),self)
        self.dock1.setFeatures(QDockWidget.DockWidgetMovable)
        self.dock1.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)

        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 561, 161))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 561, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab, "内存")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 561, 141))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab_2, "硬盘")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 0, 561, 141))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_3, "CPU")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(0, 0, 561, 141))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.tabWidget.addTab(self.tab_4, "未启动服务")

        self.dock1.setFixedWidth(250)
        #te2=QTextEdit(self.tr("窗口2,可在Main Window的左部和右部停靠，不可浮动，不可关闭"))
        self.dock1.setWidget(self.tabWidget)
        self.parent().addDockWidget(Qt.RightDockWidgetArea,self.dock1)
