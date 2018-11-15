import paramiko,time
class LinuxUtil():
    def __init__(self):
        self.hostname = '43.4.112.155'
        self.username = 'admin123'
        self.pwd = 'admin123'

    def sshclient_execmd(self, execmd):
        paramiko.util.log_to_file("paramiko.log")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            s.connect(hostname=self.hostname, port=22, username=self.username, password=self.pwd, timeout=2)
            stdin, stdout, stderr = s.exec_command (execmd)
            stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
            result = ''
            for line in stdout:
                result+=line
                #print (line.strip('\n'))
            s.close()
        except Exception as e:
            print(e)
            result = "连接超时"
        return result
    def get_free(self):
        paramiko.util.log_to_file("paramiko.log")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            s.connect(hostname=self.hostname, port=22, username=self.username, password=self.pwd, timeout=2)
            stdin, stdout, stderr = s.exec_command ('free -h')
            stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
            result = ''
            for i,line in enumerate(stdout):
                reusltArr = line.split()
                if 1==i:
                    result+='总量(total)：'+reusltArr[1]+'\n\n'+'使用量(used)：'+reusltArr[2]+'\n\n'+'可用量(available)：'+reusltArr[6]
            s.close()
        except Exception as e:
            print(e)
            result = "连接超时"
        return result

    def get_cpu(self):
        paramiko.util.log_to_file("paramiko.log")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            s.connect(hostname=self.hostname, port=22, username=self.username, password=self.pwd, timeout=2)
            stdin, stdout, stderr = s.exec_command('top -b -n 1')
            #stdin, stdout, stderr = s.exec_command ('top')
            stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
            result = ''
            for i,line in enumerate(stdout):
                reusltArr = line.split()
                #print(reusltArr)
                if len(reusltArr) == 12:
                    #print(len(reusltArr))
                    if reusltArr[8] != '0.0' and reusltArr[9] != '0.0':
                        if 'COMMAND'!=reusltArr[11]:
                            result+=reusltArr[11]+':(CPU)'+reusltArr[8]+'%  (MEM)'+reusltArr[9]+'%\n\n'
                    #print(reusltArr)
            s.close()
        except Exception as e:
            print(e)
            result = "连接超时"
        return result
    def get_hard(self):
        paramiko.util.log_to_file("paramiko.log")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            s.connect(hostname=self.hostname, port=22, username=self.username, password=self.pwd, timeout=2)
            stdin, stdout, stderr = s.exec_command ('df -h /')
            stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
            result = ''
            for i,line in enumerate(stdout):
                reusltArr = line.split()
                if 1==i:
                    result+='总量(Size)：'+reusltArr[1]+'\n\n'+'使用量(used)：'+reusltArr[2]+'\n\n'+'可用量(available)：'+reusltArr[3]+'\n\n'+'使用百分比(Use%)：'+reusltArr[4]
            s.close()
        except Exception as e:
            print(e)
            result = "连接超时"
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
    #result = util.get_cpu()
   # print(result)
    #util.sshclient_execmd('df -m /') ##硬盘使用情况
    result = util.get_cpu() ##硬盘使用情况
    print(result)
    #util.sshclient_logcmd()
    #sftp_upload("43.4.112.155",22,"admin123","admin123")

    # s = paramiko.SSHClient()
    # s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # flag = s.connect(hostname="43.4.112.155", port=22, username="admin", password="admin", timeout=1)
    # stdin, stdout, stderr = s.exec_command ("ls")
    # print(stderr)
