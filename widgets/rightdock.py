# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from  widgets.ui.rightdock import Ui_Form
#删除员工信息
class rightDock(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(rightDock, self).__init__()
        self.setupUi(self)
