# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from  widgets.ui.resourceManage import Ui_Form
from  util.linux_util import LinuxUtil
from widgets.load import loadingDlg
import time
#删除员工信息
class resource_manage(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(resource_manage, self).__init__()
        self.setupUi(self)
        self.loading = loadingDlg()
        self.loading.exec()
        time.sleep(5)
        #self.init_data()
        self.loading.destroy()

    def init_data(self):
        util = LinuxUtil()
        mem_result = util.sshclient_execmd("free -m")
        hard_result = util.sshclient_execmd("df -m /")
        self.mem.setText(mem_result)
        self.hard.setText(hard_result)
