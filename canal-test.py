import pymysql
import time
import random

conn = pymysql.connect(
    host='rm-2ze0806f9c96lksh8120.mysql.rds.aliyuncs.com',
    user='jindi_yunwei_rw', password='FXLXCxKyOn63A9l',
    database='liuguangcheng',
    charset='utf8')
conn.autocommit(1)
cursor = conn.cursor()
while True:
    time.sleep(1)
    num = random.randint(0, 100)
    sql = f"insert into user_college(user_id) values ({num})"
    print(sql)
    cursor.execute(sql)
