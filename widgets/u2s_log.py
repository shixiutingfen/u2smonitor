# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from  widgets.ui.logUI import Ui_Form
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#删除员工信息
class u2s_log(QtWidgets.QWidget,Ui_Form):
    myControls ={}
    def __init__(self):
        super(u2s_log, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('TreeWidget')
        #self.treeWidget = QTreeWidget()
        self.myControls['treeWidget']=self.treeWidget
        self.treeWidget.setColumnCount(2) # 说明是树形的表，
        self.treeWidget.setHeaderLabels(['Key','Value']) # 是表，则有表头
        # 根节点的父是 QTreeWidget对象
        root= QTreeWidgetItem(self.treeWidget)

        root.setText(0,'root')
        child1 = QTreeWidgetItem(root) #指出父结点
        child1.setText(0,'child1')
        child1.setText(1,'name1')
        child2 = QTreeWidgetItem(root)
        child2.setText(0,'child2')
        child2.setText(1,'name2')
        child3 = QTreeWidgetItem(root)
        child3.setText(0,'child3')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0,'child4')
        child4.setText(1,'name4')



        #以下两句是主窗口的设置
        #self.treeWidget.addTopLevelItem(root)

