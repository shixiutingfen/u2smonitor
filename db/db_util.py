# -*- coding: utf-8 -*-
import  pymysql
class DbUtil():
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "Ast4HS", db="personnel_man",port=3307)

    def get_unresolve_task(self):
         # 打开数据库
        cursor = self.db.cursor()
        try:
            cursor.execute("select s_no,s_name from staff order by convert (s_no,signed)")
            results = cursor.fetchall()
            return  results
        except Exception as e:
            print(e)