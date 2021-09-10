import pymysql
import time
import random

conn = pymysql.connect(
    host='xxx',
    user='xxx', password='xxx',
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
