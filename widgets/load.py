from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
import threading
class loadingDlg(QDialog):
    def __init__(self,parent=None):
        super(loadingDlg, self).__init__(parent)
        self.label = QLabel('Red', self)
        self.setFixedSize(200,200)
       # self.setWindowOpacity(0.5)
        self.setWindowFlags(QtCore.Qt.Dialog|QtCore.Qt.CustomizeWindowHint)
        #self.setContentsMargins(0,0,0,0)
        #self.label.setContentsMargins(0,0,0,0)

        self.movie = QMovie("D:/workspace_python/u2smonitor/widgets/loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label.show()
    def destroyDlg(self):
        self.close ()
         

