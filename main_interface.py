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



#主界面
class staff_Admin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(staff_Admin, self).__init__()
        self.setupUi(self)
        grid = QtWidgets.QGridLayout()
        self.content.setLayout(grid)

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