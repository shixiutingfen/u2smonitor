import sqlite3
class SqliteUtil():
    def __init__(self):
        self.conn =  sqlite3.connect("D:/workspace_python/u2smonitor/sqlite.db")

    def get_cursor(self):
        if self.conn is not None:
            return self.conn.cursor()
        else:
            return sqlite3.connect("sqlite.db").cursor()
    def close_all(self, cu):
        '''关闭数据库游标对象和数据库连接对象'''
        try:
            if cu is not None:
                cu.close()
        finally:
            if cu is not None:
                cu.close()

    def drop_table(self, table):
        '''如果表存在,则删除表，如果表中存在数据的时候，使用该
        方法的时候要慎用！'''
        if table is not None and table != '':
            sql = 'DROP TABLE IF EXISTS ' + table
            print('执行sql:[{}]'.format(sql))
            cu = self.get_cursor()
            cu.execute(sql)
            self.conn.commit()
            print('删除数据库表[{}]成功!'.format(table))
            self.close_all(cu)
        else:
            print('the [{}] is empty or equal None!')
    def create_table(self, sql):
        '''创建数据库表：student'''
        if sql is not None and sql != '':
            cu = self.get_cursor()
            print('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            self.conn.commit()
            self.close_all(cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def save(self, sql, data):
        '''插入数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor()
                for d in data:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    self.conn.commit()
                self.close_all( cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchall(self, sql):
        '''查询所有数据'''
        if sql is not None and sql != '':
            cu = self.get_cursor()
            print('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            r = cu.fetchall()
            return r
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchone(self, sql, data):
        '''查询一条数据'''
        if sql is not None and sql != '':
            if data is not None:
                #Do this instead
                d = (data,)
                cu = self.get_cursor()
                print('执行sql:[{}],参数:[{}]'.format(sql, data))
                cu.execute(sql, d)
                r = cu.fetchall()
                if len(r) > 0:
                    for e in range(len(r)):
                        print(r[e])
            else:
                print('the [{}] equal None!'.format(data))
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def update(self, sql, data):
        '''更新数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor()
                for d in data:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    self.conn.commit()
                self.close_all( cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def delete(self, sql, data):
        '''删除数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor()
                for d in data:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    self.conn.commit()
                self.close_all( cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    ###############################################################
    ####            测试操作     START
    ###############################################################
    def create_table_test(self):
        '''创建数据库表测试'''
        print('创建数据库表测试...')
        create_table_sql = '''CREATE TABLE `student` (
                              `id` int(11) NOT NULL,
                              `name` varchar(20) NOT NULL,
                              `gender` varchar(4) DEFAULT NULL,
                              `age` int(11) DEFAULT NULL,
                              `address` varchar(200) DEFAULT NULL,
                              `phone` varchar(20) DEFAULT NULL,
                               PRIMARY KEY (`id`)
                            )'''
        self.create_table( create_table_sql)

    def save_test(self):
        '''保存数据测试...'''
        print('保存数据测试...')
        save_sql = '''INSERT INTO student values (?, ?, ?, ?, ?, ?)'''
        data = [(1, 'Hongten', '男', 20, '广东省广州市', '13423****62'),
                (2, 'Tom', '男', 22, '美国旧金山', '15423****63'),
                (3, 'Jake', '女', 18, '广东省广州市', '18823****87'),
                (4, 'Cate', '女', 21, '广东省广州市', '14323****32')]
        self.save( save_sql, data)

    def fetchall_test(self):
        '''查询所有数据...'''
        print('查询所有数据...')
        fetchall_sql = '''SELECT * FROM student'''
        self.fetchall( fetchall_sql)

    def fetchone_test(self):
        '''查询一条数据...'''
        print('查询一条数据...')
        fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
        data = 1
        self.fetchone( fetchone_sql, data)

    def update_test(self):
        '''更新数据...'''
        print('更新数据...')
        update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
        data = [('HongtenAA', 1),
                ('HongtenBB', 2),
                ('HongtenCC', 3),
                ('HongtenDD', 4)]
        self.update( update_sql, data)

    def delete_test(self):
        '''删除数据...'''
        print('删除数据...')
        delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
        data = [('HongtenAA', 1),
                ('HongtenCC', 3)]
        self.delete( delete_sql, data)

if __name__ == '__main__':
    util = SqliteUtil()
    sql = "select * FROM  linux_address"
    print(util.fetchall(sql))
    #util.drop_table('linux_address')
    #util.create_table_test()
    #util.save_test()
    #util.update_test()
    #util.fetchall_test()
    #util.fetchone_test()
    #util.delete_test()
