import json

import pymysql

import config

# 数据库配置字典
mysql_config = {
    "host": config.host,
    "port": config.port,
    "userName": config.name,
    "password": config.password,
    "dbName": config.dbname,
    "charsets": "utf8mb4"
}


class MySqlUtil:
    """mysql数据库工具类
    1.自动获取游标
    2.自动关闭数据库连接
    3.执行sql
    """
    db = None
    cursor = None

    def __init__(self):
        self.host = mysql_config['host']
        self.port = mysql_config['port']
        self.userName = mysql_config['userName']
        self.password = mysql_config['password']
        self.dbName = mysql_config['dbName']
        self.charsets = mysql_config['charsets']

    def get_connect(self):
        """ 获取数据库Connect """
        self.db = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.userName,
            passwd=self.password,
            db=self.dbName,
            charset=self.charsets
        )
        self.cursor = self.db.cursor()

    def close(self):
        """关闭数据库连接"""
        self.cursor.close()
        self.db.close()

    def get_one(self, sql, param=None):
        """
        查询单条数据
        :param sql: 查询sql
        :param param: 参数
        :return: 查询结果
        """
        res = None
        try:
            self.get_connect()
            if param is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, param)
            res = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print("查询失败:" + str(e))
        return res

    def get_all(self, sql, param=None):
        """
         查询列表数据
        :param sql:  查询sql
        :param param:  参数
        :return:查询结果
        """
        res = None
        try:
            self.get_connect()
            if param is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, param)
            res = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print("查询失败:" + str(e))
        return res

    def save(self, sql, param=None):
        """
        保存数据
        :param sql: insert的sql语句
        :param param: 参数
        :return: 最新保存信息的id
        """
        id = None
        try:
            self.get_connect()
            if param is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, param)
            self.db.commit()
            id = self.cursor.lastrowid
            self.close()
        except Exception as e:
            print("操作失败:" + str(e))
            self.db.rollback()
        return id
