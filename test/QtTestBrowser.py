import sys
from PyQt4 import QtGui,QtCore
import time
import random
from PyQt4.QtCore import QTimer
class MyThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def run_(self, message):
        #time.sleep(random.random() * 5)
        self.trigger.emit(message)


class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.text_area = QtGui.QTextBrowser()
        self.thread_button = QtGui.QPushButton('Start threads')
        self.thread_button.clicked.connect(self.start_threads)

        central_widget = QtGui.QWidget()
        central_layout = QtGui.QHBoxLayout()
        central_layout.addWidget(self.text_area)
        central_layout.addWidget(self.thread_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        #self.threads = MyThread(self)
       # self.threads.trigger.connect(self.update_text)

        self.thread_no = 0

    def start_threads(self):
        # self.thread_no += 1
        # message = "cnt:{0}".format(self.thread_no)
        # self.threads.run_(message)  # start the thread
        # print(message)
        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.oprate) #计时结束调用operate()方法
        self.timer.start(2000) #设置计时间隔并启动
    def oprate(self):
        print(1111)
    def update_text(self, message):
        # self.text_area.append('thread # %d finished'%thread_no)
        # print('thread # %d finished'%thread_no)
        self.text_area.clear()
        self.text_area.append(message)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mainWindow = Main()
    mainWindow.show()

    sys.exit(app.exec_())
