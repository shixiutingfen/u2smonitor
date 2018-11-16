# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from  widgets.ui.unresolveUi import Ui_Form
from  widgets.ui.taskdetail import Ui_Form as Ui_FormTaskDetail
from  db.db_util import DbUtil
from PyQt5.QtWidgets import QTableWidgetItem,QHeaderView
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QCursor
from functools import partial
#删除员工信息
class un_resolved(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(un_resolved, self).__init__()
        self.setupUi(self)
        self.initTable()

    def initTable(self):
        dbutil = DbUtil()
        results = dbutil.get_unresolve_task()
        obj={}
        for row in results:
                    TASK_ID = row[0]
                    ANALYSIS_TASK_ID = row[1]
                    SUBMIT_TIME = row[2]
                    USER_DATA = row[3]
                    oldrow = self.tableWidget.rowCount()
                    self.tableWidget.setRowCount(oldrow + 1)

                    item = QTableWidgetItem(str(TASK_ID))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(str(ANALYSIS_TASK_ID))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 1, item)

                    item = QTableWidgetItem(str(SUBMIT_TIME))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 2, item)

                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()


                    obj[strbtn].setText("详细信息")
                    obj[strbtn].setStyleSheet("text-decoration: underline")

                    self.one = partial(self.btnclicked, obj[strbtn])
                    #print(btn.objectName())
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.tableWidget.setCellWidget(oldrow,3,obj[strbtn])
                    obj[strbtn].clicked.connect(self.one)
                    self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

         #点击删除按钮
    def btnclicked(self,btn):
        x = btn.frameGeometry().x()
        y = btn.frameGeometry().y()
        index = self.tableWidget.indexAt(QPoint(x, y))
        row = index.row()
        taskid = self.tableWidget.item(row, 0).text()  # 获取部门编号
        serinum = self.tableWidget.item(row, 1).text()
        print(taskid)
        print(serinum)
        for singer_obj in self.parent().children():
            if isinstance(singer_obj, QtWidgets.QGridLayout) == True:
                grid = singer_obj
        content = self.parent()
        for singer_obj in content.children():
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,QtWidgets.QGridLayout) == False):
                singer_obj.hide()

        content.taskDetail = TaskDetail()

        grid.addWidget(content.taskDetail)
        content.taskDetail.label.setText(serinum)

#删除员工信息
class TaskDetail(QtWidgets.QWidget,Ui_FormTaskDetail):
    def __init__(self):
        super(TaskDetail, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goback)
    #返回按钮
    def goback(self):
        for singer_obj in self.parent().children():
            if isinstance(singer_obj, QtWidgets.QGridLayout) == True:
                grid = singer_obj

        content = self.parent()
        for singer_obj in content.children():
            # print(singer_obj.objectName())
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,QtWidgets.QGridLayout) == False):
                grid.removeWidget(singer_obj)
                singer_obj.deleteLater()
        self.un_resolved_page = un_resolved()
        grid.addWidget(self.un_resolved_page)
