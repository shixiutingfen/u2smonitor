import paramiko
from sqllite_util import SqliteUtil
class LinuxUtil():
    def __init__(self):
        self.hostname = '43.4.112.155'
        self.username = 'admin123'
        self.pwd = 'admin123'

    def sshclient_execmd(self, execmd):
        paramiko.util.log_to_file("paramiko.log")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=self.hostname, port=22, username=self.username, password=self.pwd)
        stdin, stdout, stderr = s.exec_command (execmd)
        stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
        result = ''
        for line in stdout:
            result+=line
            #print (line.strip('\n'))
        s.close()
        return result

    def sftp_upload(ip,port,user,pwd):
        client = paramiko.Transport((ip,port))
        client.connect(username=user,password=pwd)
        sftp = paramiko.SFTPClient.from_transport(client)
        remote_path = "/u2s/slave/objext/objext/log/vasdk/2018-10-29/11.09.41_201810291027150104303122/VASDK-analysis.log"
        local_path = "D:/VASDK-analysis.log"
        # 使用paramiko下载文件到本机
        sftp.get(remote_path, local_path)
        client.close()

    def sshclient_logcmd(self):
        paramiko.util.log_to_file("paramiko.log")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=self.hostname, port=22, username=self.username, password=self.pwd)
        stdin, stdout, stderr = s.exec_command ("free -m ")
        stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
        for line in stdout:
            print (line.strip('\n'))
        s.close()
if __name__ == "__main__":
    util = LinuxUtil()
    #util.sshclient_execmd('free -m') ##内存使用情况
    #util.sshclient_execmd('df -m /') ##硬盘使用情况
    result = util.sshclient_execmd('free -m') ##硬盘使用情况
    print(result)
    #util.sshclient_logcmd()
    #sftp_upload("43.4.112.155",22,"admin123","admin123")
