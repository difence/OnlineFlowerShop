import pymssql

import tool.fun


class sqlClient:
    def __init__(self, host, port, dataBase, user, password):
        self.connection = None
        self.host = host
        self.port = port
        self.db = dataBase
        self.user = user
        self.password = password
        self.connection: pymssql.connect

    def setConnection(self):
        try:
            self.connection = pymssql.connect('{}:{}'.format(self.host, self.port), self.user, self.password)
            tool.fun.logFormat(tool.fun.INFO, '成功连接数据库')
        except:
            tool.fun.logFormat(tool.fun.WARN, '数据库连接失败')
            exit(0)

    def insertInfo(self, table, args):
        cur = self.connection.cursor()
        if type(args) == list:
            value = ''
            for i in args:
                value += ("\'{}\',".format(str(i)))
            value = '({})'.format(value[:-1])
            sqlString = 'insert into {}.dbo.{} values {}'.format(self.db, table, value)
        else:
            att = ''
            for i in args.keys():
                att += '{} ,'.format(i)
            att = '({})'.format(att[:-1])

            value = ''
            for i in args.keys():
                value += '\'{}\','.format(args[i])
            value = '({})'.format(value[:-1])
            sqlString = 'insert into {}.dbo.{}{} values {}'.format(self.db, table, att, value)
        cur.execute(sqlString)
        self.connection.commit()
        tool.fun.logFormat(tool.fun.INFO, "在表 {} 插入数据 {}".format(table, value))

    def delInfo(self, table, _id):
        value = 'delete from {}.dbo.{} where id = {}'.format(self.db, table, _id)
        cur = self.connection.cursor()
        cur.execute(value)
        self.connection.commit()
        tool.fun.logFormat(tool.fun.INFO, value)

    def searchInfo(self, table, attrs=None, val=None, mult=False):
        if attrs is None:
            attrs = ''
        if val is None:
            val = []
        sel = ''
        for i in val:
            sel += '{},'.format(i)
        if len(val):
            sel = '({})'.format(sel[:-1])
        else:
            sel = '*'
        if len(attrs) == 0:
            value = 'select {} from {}.dbo.{}'.format(sel, self.db, table)
        else:
            value = ''
            for i in attrs:
                value += ('{} = \'{}\' and '.format(i, attrs[i]))
            value = 'select {} from {}.dbo.{} where {}'.format(sel, self.db, table, value[:-4])
        cur = self.connection.cursor()
        cur.execute(value)
        res = cur.fetchall()
        if not mult:
            res = res[0]
        tool.fun.logFormat(tool.fun.INFO, '查询 {}'.format(value))
        return res

    def isExist(self, table, attrs=None):
        if attrs is None:
            attrs = ''
        if len(attrs) == 0:
            value = 'select * from {}.dbo.{}'.format(self.db, table)
        else:
            value = ''
            for i in attrs:
                value += ('{} = \'{}\' and '.format(i, attrs[i]))
            value = 'select * from {}.dbo.{} where {}'.format(self.db, table, value[:-4])
        cur = self.connection.cursor()
        cur.execute(value)
        res = cur.fetchall()
        tool.fun.logFormat(tool.fun.INFO, '在表 {} 查询 {} 是否存在'.format(table, attrs))
        if len(res) > 0:
            return True
        else:
            return False

    def update(self, table, attrs: dict, val: dict):
        att = ''
        for i in attrs:
            att += '{} = \'{}\' and'.format(i, attrs[i])
        att = att[:-3]

        valu = ''
        for i in val:
            valu += '{} = \'{}\' and'.format(i, val[i])
        valu = valu[:-3]

        value = 'update {}.dbo.{} set {} where {}'.format(self.db, table, valu, att)
        cur = self.connection.cursor()
        cur.execute(value)
        self.connection.commit()
        tool.fun.logFormat(tool.fun.INFO, '修改 {}'.format(value))
