# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from  widgets.ui.unresolveUi import Ui_Form
from  db.db_util import DbUtil
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
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
                    sno = row[0]
                    sname = row[1]

                    oldrow = self.tableWidget.rowCount()
                    self.tableWidget.setRowCount(oldrow + 1)

                    item = QTableWidgetItem(str(sno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 1, item)

                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()


                    obj[strbtn].setText("详细信息")
                    obj[strbtn].setStyleSheet("text-decoration: underline")

                    self.one = partial(self.btnclicked, obj[strbtn])
                    #print(btn.objectName())
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.tableWidget.setCellWidget(oldrow,2,obj[strbtn])
                    obj[strbtn].clicked.connect(self.one)

         #点击删除按钮
    def btnclicked(self,btn):
        print(btn)