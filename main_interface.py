import  sys
import  pymysql
import datetime
import re
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QAction,QMenu,QAbstractItemView
from mainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QCursor
from functools import partial
from login import  Ui_login
from widgets.u2s_log import u2s_log
from widgets.resource_manage import resource_manage
from widgets.un_resolved import un_resolved
from sqllite_util import SqliteUtil
import sip
from widgets.rightdock import rightDock
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

#主界面
class staff_Admin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(staff_Admin, self).__init__()
        self.setupUi(self)
        grid = QtWidgets.QGridLayout()
        self.content.setLayout(grid)
        self.initDock()

        #self.dock
    def test(self):
        self.label1.show()
        self.label2.show()
        db = pymysql.connect("localhost", "root", "Ast4HS", db="personnel_man",port=3307)
        txt = self.treeWidget.currentItem().text(0)
        grid = self.content.layout()

        if txt!='部门信息' and txt!='考核管理' and txt!='人事管理' and txt!='薪资管理' and txt!='员工信息':
            for singer_obj in self.content.children():
                #print("初始",singer_obj)
                if(isinstance(singer_obj,QtWidgets.QLabel)==False and isinstance(singer_obj,QtWidgets.QGridLayout)==False):
                    grid.removeWidget(singer_obj)
                    singer_obj.deleteLater()
                    #sip.delete(singer_obj)
        else:
            self.label1.hide()
            self.label2.hide()

        if txt == '资源管理':
            self.label1.hide()
            self.label2.hide()
            try:
                self.resourceManage = resource_manage()
                grid.addWidget(self.resourceManage)
            except Exception as e:
                print(e)

        elif txt =='日志管理':
            self.label1.hide()
            self.label2.hide()
            try:
                 self.u2sLog = u2s_log()
                 grid.addWidget(self.u2sLog)
            except Exception as e:
                print(e)

        elif txt =='未完成任务':
            self.label1.hide()
            self.label2.hide()
            try:
                 self.unresolved = un_resolved()
                 grid.addWidget(self.unresolved)
            except Exception as e:
                print(e)
    def initDock(self):
        #停靠窗口1
        dock1=QDockWidget(self.tr("系统状态"),self)
        dock1.setFeatures(QDockWidget.DockWidgetMovable)
        dock1.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)

        tabWidget = QtWidgets.QTabWidget()
        tabWidget.setGeometry(QtCore.QRect(10, 0, 561, 161))
        tabWidget.setObjectName("tabWidget")
        tab = QtWidgets.QWidget()
        tab.setObjectName("tab")
        textBrowser = QtWidgets.QTextBrowser(tab)
        textBrowser.setGeometry(QtCore.QRect(0, 0, 561, 141))
        textBrowser.setObjectName("textBrowser")
        tabWidget.addTab(tab, "内存")
        tab_2 = QtWidgets.QWidget()
        tab_2.setObjectName("tab_2")
        textBrowser_2 = QtWidgets.QTextBrowser(tab_2)
        textBrowser_2.setGeometry(QtCore.QRect(0, 0, 561, 141))
        textBrowser_2.setObjectName("textBrowser_2")
        tabWidget.addTab(tab_2, "硬盘")
        tab_3 = QtWidgets.QWidget()
        tab_3.setObjectName("tab_3")
        textBrowser_3 = QtWidgets.QTextBrowser(tab_3)
        textBrowser_3.setGeometry(QtCore.QRect(0, 0, 561, 141))
        textBrowser_3.setObjectName("textBrowser_3")
        tabWidget.addTab(tab_3, "CPU")
        tab_4 = QtWidgets.QWidget()
        tab_4.setObjectName("tab_4")
        textBrowser_4 = QtWidgets.QTextBrowser(tab_4)
        textBrowser_4.setGeometry(QtCore.QRect(0, 0, 561, 141))
        textBrowser_4.setObjectName("textBrowser_4")
        tabWidget.addTab(tab_4, "未启动服务")

        dock1.setFixedWidth(250)
        #te2=QTextEdit(self.tr("窗口2,可在Main Window的左部和右部停靠，不可浮动，不可关闭"))
        dock1.setWidget(tabWidget)
        self.addDockWidget(Qt.RightDockWidgetArea,dock1)
#登陆
class login(QtWidgets.QDialog,Ui_login):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)
        util = SqliteUtil()
        results = util.fetchall("select * from linux_address ORDER BY createtime DESC ")
        ip = results[0][0]
        username = results[0][1]
        pwd = results[0][2]
        self.ip.setText(ip)
        self.username.setText(username)
        self.pwd.setText(pwd)
    def jump(self):
        try:
            self.close()
            ipcon = self.ip.text()
            usernamecon = self.username.text()
            pwdcon = self.pwd.text()
            util = SqliteUtil()
            sql = "select * from linux_address where ip='"+ipcon+"' and username='"+usernamecon+"' and pwd='"+pwdcon+"'"
            results = util.fetchall(sql)
            if len(results) == 0:#不存在
                save_sql = '''INSERT INTO linux_address values (?, ?, ?, ?)'''
                nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data = [(ipcon,usernamecon,pwdcon, nowtime)]
                util.save( save_sql, data)
            self.my_staffAdmin = staff_Admin()
            self.my_staffAdmin.show()
        except:
            print("error")


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = login()
    login_window.show()
    sys.exit(app.exec_())