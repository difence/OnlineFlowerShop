import pymssql
import pymysql

import fun


class sqlClient:
    def __init__(self, host, port, dataBase, user, password):
        self.connection = None
        self.host = host
        self.port = port
        self.db = dataBase
        self.user = user
        self.password = password
        self.connection: pymysql.connect

    def setConnection(self):
        try:
            self.connection = pymssql.connect('{}:{}'.format(self.host, self.port), self.user, self.password)
            fun.logFormat(fun.INFO, '成功连接数据库')
        except:
            fun.logFormat(fun.WARN, '数据库连接失败')
            exit(0)

    def addInfo(self, table, args):
        value = ''
        for i in args:
            value += ("\'{}\',".format(str(i)))
        value = '({})'.format(value[:-1])
        cur = self.connection.cursor()
        cur.execute('insert into {}.dbo.{} values {}'.format(self.db, table, value))
        self.connection.commit()
        fun.logFormat(fun.INFO, "在表 {} 插入数据 {}".format(table, value))

    def delInfo(self, table, id):
        value = 'delete from {}.dbo.{} where id = {}'.format(self.db, table, id)
        cur = self.connection.cursor()
        cur.execute(value)
        self.connection.commit()
        fun.logFormat(fun.INFO, "在表 {} 刪除数据 {}".format(table, id))

    def searchInfo(self, table, attrs=None):
        if attrs is None:
            attrs = ''
        if len(attrs) == 0:
            value = 'select * from {}.dbo.{}'.format(self.db, table)
        else:
            value = ''
            for i in attrs:
                value += ('{} = \'{}\' and'.format(i, attrs[i]))
            value = 'select * from {}.dbo.{} where {}'.format(self.db, table, value[:-4])
        cur = self.connection.cursor()
        cur.execute(value)
        res = cur.fetchall()
        fun.logFormat(fun.INFO, '在表 {} 查找数据 {}'.format(table, attrs))
        return res
