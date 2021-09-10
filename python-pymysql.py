# -*- coding:utf-8 -*-
import pymysql

'''1.数据库查询操作'''
db = pymysql.connect("localhost","root","root","hd_20190424")  # 地址，用户名，密码，数据库名

# 使用cursor()方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用execute()方法执行sql语句
cursor.execute("select version()")

# 使用fetchone()方法获取单条数据
data = cursor.fetchone()

print("database version:%s" % data)

# 关闭数据库连接
db.close()

'''2.数据库插入操作'''

# 打开数据库连接
db = pymysql.connect("localhost","root","root","hd_20190424")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO hd_20190424(username,age)VALUES ('wangyifan', 25)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
