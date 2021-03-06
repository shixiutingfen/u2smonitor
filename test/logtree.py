import sys
import paramiko
from PyQt5.QtWidgets import *
class TreeWidget(QMainWindow):  
    myControls ={}  
    def __init__(self,parent=None):  
        QWidget.__init__(self,parent)  
        self.setWindowTitle('TreeWidget')  
        self.tree = QTreeWidget()  
        self.myControls['tree']=self.tree  
        self.tree.setColumnCount(2) # 说明是树形的表，
        self.tree.setColumnWidth(400,200)
        self.tree.setHeaderLabels(['文件名','全路径']) # 是表，则有表头
        paramiko.util.log_to_file("paramiko.log")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname="43.4.112.155", port=22, username="admin123", password="admin123")
        stdin, stdout, stderr = s.exec_command ("cd /u2s/slave/objext/objext/log;ls")
        stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
        for line in stdout:
            # 根节点的父是 QTreeWidget对象
            root= QTreeWidgetItem(self.tree)
            root.setText(0,line)
            self.tree.addTopLevelItem(root)
            cmd = "cd /u2s/slave/objext/objext/log/"+line.strip()+";ls"
            stdin2, stdout2, stderr2  = s.exec_command (cmd)
            for line2 in stdout2:
                child1 = QTreeWidgetItem(root) #指出父结点
                child1.setText(0,line2)
                child1.setText(1,'')
                cmd2 = "cd /u2s/slave/objext/objext/log/"+line.strip()+"/"+line2.strip()+";ls"
                stdin3, stdout3, stderr3  = s.exec_command (cmd2)
                for line3 in stdout3:
                     child2 = QTreeWidgetItem(child1)
                     child2.setText(0,line3)
                     child2.setText(1,"/u2s/slave/objext/objext/log/"+line.strip()+"/"+line2.strip()+"/"+line3.strip())
                     if str(line).find("vasdk")>=0:
                            cmd3 = "cd /u2s/slave/objext/objext/log/"+line.strip()+"/"+line2.strip()+"/"+line3.strip()+";ls"
                            stdin4, stdout4, stderr4  = s.exec_command (cmd3)
                            for line4 in stdout4:
                                 child3 = QTreeWidgetItem(child2)
                                 child3.setText(0,line4)
                                 child3.setText(1,"/u2s/slave/objext/objext/log/"+line.strip()+"/"+line2.strip()+"/"+line3.strip()+"/"+line4.strip())

        s.close()
        #以下两句是主窗口的设置  
        self.setCentralWidget(self.tree)
        self.tree.doubleClicked.connect(self.onClicked)

    def sftp_upload(ip,filepath,local_path):
        client = paramiko.Transport(("43.4.112.155",22))
        client.connect(username="admin123",password="admin123")
        sftp = paramiko.SFTPClient.from_transport(client)
        # 使用paramiko下载文件到本机
        sftp.get(filepath, local_path)
        client.close()
    def onClicked(self,qmodeLindex):
        fileDirectory = QFileDialog.getExistingDirectory()
        item=self.tree.currentItem()
        localpath = fileDirectory+"/"+item.text(0)
        self.sftp_upload(item.text(1),localpath.strip())
        print('Key=%s,value=%s'%(item.text(0),item.text(1)))
  
app = QApplication(sys.argv)  
tp = TreeWidget()  
tp.show()  
app.exec_() 