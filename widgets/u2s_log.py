# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from  widgets.ui.logUI import Ui_Form
#删除员工信息
class u2s_log(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(u2s_log, self).__init__()
        self.setupUi(self)