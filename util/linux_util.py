import paramiko,time
from sqllite_util import SqliteUtil
class LinuxUtil():
    def __init__(self):
        util = SqliteUtil()
        results = util.fetchall("select * from linux_address ORDER BY createtime DESC ")
        self.hostname = results[0][0]
        print(self.hostname)
        self.username = results[0][1]
        self.pwd = results[0][2]
        # self.hostname = '43.4.112.155'
        # self.username = 'admin123'
        # self.pwd = 'admin123'

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
    def get_unstart_service(self):
        sqlliteutil = SqliteUtil()
        paramiko.util.log_to_file("paramiko.log")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        resultstr = ''
        try:
            s.connect(hostname=self.hostname, port=22, username=self.username, password=self.pwd, timeout=2)
            results = sqlliteutil.fetchall("select * from service_names ")
            for result in results:
                cmd = 'service '+result[2]+' status'
                stdin, stdout, stderr = s.exec_command (cmd)
                stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction
                outstr = str(stdout.read())
                if outstr.find('inactive')>0 or  outstr.find('failed')>0:
                    resultstr+=result[1]+'\n\n'

        except Exception as e:
            print(e)
            resultstr = "连接超时"
        s.close()
        return resultstr
    def get_versioninf(self):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        resultstr = ''
        try:
            s.connect(hostname=self.hostname, port=22, username=self.username, password=self.pwd, timeout=2)
            stdin, stdout, stderr = s.exec_command ('ls -lih /u2s/slave/objext/objext/VideoObjectExtractionService')
            stdin2, stdout2, stderr2 = s.exec_command ('ls -lih /u2s/slave/objext/objext/libImageRecog_jni.so')
            stdin3, stdout3, stderr3 = s.exec_command ('ls -lih /u2s/slave/objext/objext/libVideoAnalysisSDK.so')
            stdin4, stdout4, stderr4 = s.exec_command ('ls -lih /u2s/slave/objext/objext/OESObjectHandlerManager.so')
            stdin5, stdout5, stderr5 = s.exec_command ('ls -lih /u2s/slave/objext/objext/OESObjectKafkaHandler.so')
            stdin6, stdout6, stderr6 = s.exec_command ('ls -lih /u2s/slave/objext/objext/OESObjectRabbitMQHandler.so')
            VideoObjectExtractionService = str(stdout.read())
            libImageRecog_jni = str(stdout2.read())
            #print(libImageRecog_jni)
            libVideoAnalysisSDK = str(stdout3.read())
            OESObjectHandlerManager = str(stdout4.read())
            OESObjectKafkaHandler = str(stdout5.read())
            OESObjectRabbitMQHandler = str(stdout6.read())
            resultstr+=VideoObjectExtractionService.split('->')[1].strip()+"\n\n"+libImageRecog_jni.split('->')[1]+'\n\n'+libVideoAnalysisSDK.split('->')[1]+'\n\n'+OESObjectHandlerManager.split('->')[1]\
                       +'\n\n'+OESObjectKafkaHandler.split('->')[1]+'\n\n'+OESObjectRabbitMQHandler.split('->')[1]
            s.close()
        except Exception as e:
            print(e)
            resultstr = "连接超时"
        return resultstr
    def sftp_upload(self,ip,port,user,pwd):
        client = paramiko.Transport((ip,port))
        client.connect(username=user,password=pwd)
        sftp = paramiko.SFTPClient.from_transport(client)
        remote_path = "/u2s/manager/apache-tomcat-8.5.23/logs/u2s.log"
        local_path = "D:/u2s.log"
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
    #print(result)
    #result = util.sshclient_execmd('ls -lih /u2s/slave/objext/objext/VideoObjectExtractionService') ##硬盘使用情况
    #result = util.get_cpu() ##硬盘使用情况
    #print(result)
    #util.get_unstart_service()
    #result = util.get_unstart_service()
    result = util.get_versioninf()
    #print(result)
    #util.sshclient_logcmd()
    #util.sftp_upload("43.4.112.155",22,"admin123","admin123")

    # s = paramiko.SSHClient()
    # s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # flag = s.connect(hostname="43.4.112.155", port=22, username="admin", password="admin", timeout=1)
    # stdin, stdout, stderr = s.exec_command ("ls")
    # print(stderr)
