from PyQt5.QtCore import  QThread, pyqtSignal
import time
class LogThread(QThread):
    # 定义一个信号
    logtrigger = pyqtSignal()

    def __int__(self):
        # 初始化函数，默认
        super(LogThread, self).__init__()

    def run(self):
        time.sleep(2)
        # 等待5秒后，给触发信号，并传递test
        self.logtrigger.emit()
