from PyQt5.QtCore import  QThread, pyqtSignal
import time
class DorkThread(QThread):
    # 定义一个信号
    trigger = pyqtSignal()

    def __int__(self):
        # 初始化函数，默认
        super(DorkThread, self).__init__()

    def run(self):
        time.sleep(10)
        # 等待5秒后，给触发信号，并传递test
        self.trigger.emit()
