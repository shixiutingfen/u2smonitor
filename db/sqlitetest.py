import sqlite3

conn = sqlite3.connect("sqlite.db")  #创建sqlite.db数据库
print ("open database success")
conn.execute("drop table IF EXISTS linux_address")
query = """create table IF NOT EXISTS linux_address(
    ip VARCHAR(20),
    username VARCHAR(20),
    pwd VARCHAR(20),
    createtime DATE
);"""
conn.execute(query)
print ("Table created successfully")
