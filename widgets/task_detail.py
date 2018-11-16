# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from widgets.un_resolved import un_resolved
from widgets.ui.taskdetail import Ui_Form


#删除员工信息
class TaskDetail(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(TaskDetail, self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.goback)
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
