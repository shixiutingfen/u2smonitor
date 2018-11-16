# -*- coding: utf-8 -*-
import  pymysql
from sqllite_util import SqliteUtil
class DbUtil():
    def __init__(self):
        util = SqliteUtil()
        #results = util.fetchall("select * from linux_address ORDER BY createtime DESC ")
        #hostname = results[0][0]
        self.db = pymysql.connect("43.4.112.109", "root", "123", db="u2hc",port=3306)

    def get_unresolve_task(self):
         # 打开数据库
        cursor = self.db.cursor()
        try:
            cursor.execute("select TASK_ID,ANALYSIS_TASK_ID,SUBMIT_TIME,USER_DATA from t_analysetask order by LASTUPDATE_TIME DESC limit 0,10")
            results = cursor.fetchall()
            self.db.close()
            return  results
        except Exception as e:
            print(e)