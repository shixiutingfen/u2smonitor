import  sys
import  pymysql
import datetime
import re
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QAction,QMenu,QAbstractItemView
from mainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt,QPoint,QTimer
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
from thread.dock_thread import DorkThread

#主界面
class staff_Admin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(staff_Admin, self).__init__()
        self.setupUi(self)
        grid = QtWidgets.QGridLayout()
        self.content.setLayout(grid)
        self.numcount = 0
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
        self.addDockWidget(Qt.RightDockWidgetArea,self.dock1)

        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.oprate) #计时结束调用operate()方法
        self.timer.start(5000) #设置计时间隔并启动
    def oprate(self):
        self.numcount += 1
        self.textBrowser.clear()
        self.textBrowser.append(str(self.numcount))

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