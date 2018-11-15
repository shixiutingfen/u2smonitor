import sys
from PyQt4 import QtCore,QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 160, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))


class loadingDlg(QtGui.QDialog):
    def __init__(self,parent=None):
        super(loadingDlg, self).__init__(parent)
        self.label = QtGui.QLabel('Red', self)
        self.setFixedSize(200,200)
        self.setWindowOpacity(0.5)
        self.setWindowFlags(QtCore.Qt.Dialog|QtCore.Qt.CustomizeWindowHint)
        self.setContentsMargins(0,0,0,0)
        self.label.setContentsMargins(0,0,0,0)
         
        self.movie = QtGui.QMovie("loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        #self.label.show()
    def destroyDlg(self):
        self.close ()
         
    def __del__(self):
        del self.label
        del self.movie
         
class gthread(QtCore.QThread):
    def __init__(self,parent=None):
        super(gthread, self).__init__(parent)
       
    def run(self):
        import time
        print ("thread start")
        time.sleep(2)  
 
class mainWin(QtGui.QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(mainWin,self).__init__(parent)  
        self.setupUi(self)   
         
        self.process = gthread()
        QtCore.QObject.connect(self.process, QtCore.SIGNAL("finished()"), self.finished)
        QtCore.QObject.connect(self.pushButton,  QtCore.SIGNAL('clicked()'), self.pushButtonClicked)        
 
        self.loading = loadingDlg(self)
    def pushButtonClicked(self):
        self.process.start()
        self.loading.exec_()
    def finished(self):
        print ("finished")
        self.loading.destroyDlg()
 
if __name__ == '__main__':
      
    app = QtGui.QApplication(sys.argv)
    mw = mainWin()
    mw.show()
    sys.exit(app.exec_())