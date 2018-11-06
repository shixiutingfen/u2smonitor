# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from  widgets.ui.resourceManage import Ui_Form
from  util.linux_util import LinuxUtil
#删除员工信息
class resource_manage(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(resource_manage, self).__init__()
        self.setupUi(self)
        self.init_data()

    def init_data(self):
        util = LinuxUtil()
        mem_result = util.sshclient_execmd("free -m")
        hard_result = util.sshclient_execmd("df -m /")
        self.mem.setText(mem_result)
        self.hard.setText(hard_result)
