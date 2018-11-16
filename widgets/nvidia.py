# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from  widgets.ui.nvidia import Ui_Form
from  util.linux_util import LinuxUtil
from widgets.load import loadingDlg
import time
#删除员工信息
class nvidia(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(nvidia, self).__init__()
        self.setupUi(self)
        self.init_data()

    def init_data(self):
        util = LinuxUtil()
        nvidia = util.sshclient_execmd('nvidia-smi')
        self.textBrowser.clear()
        self.textBrowser.append(nvidia)
