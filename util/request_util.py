import requests
import json
class LinuxUtil():
    def __init__(self):
        self.ip = '434243'

    def get_response(self,url,data):
        r = requests.post(url, data=data)
        return r.text

if __name__ == '__main__':
    util = LinuxUtil()
    url = "http://43.4.112.106:20280/rest/taskManage/getAllResultList"
    data = {"serialnumber":"201811081635500020243535","startTime":"2018-11-08 00:19:24","endTime":"2018-11-09 16:19:25","pageNo":"1","pageSize":"15"}
    r = requests.post(url, data=json.dumps(data))
    print(r.text)
    json_dic2 = json.dumps(r.text,indent =4 )
    print (json_dic2)
    #print(util.get_response(url,data))