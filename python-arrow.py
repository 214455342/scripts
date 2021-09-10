# -*- coding: utf-8 -*-

import arrow


'''1.获取当前时间'''
print(arrow.utcnow())  # 获取当前utc时间
print(arrow.now())   # 获取当前系统时间
print('---------------------------')

'''2.将时间戳转化为arrow对象  时间戳可以是int，float或者可以转化为float的字符串'''
print(arrow.get(1556073222))
print(arrow.get(1556073222))
print(arrow.get(1556073222.264))

print('---------------------------')

'''将字符串转换为arrow对象    arrow.get(string[,format_string])'''
print(arrow.get('2019-04-24 10:43:30','YYYY-MM-DD HH:mm:ss'))
print(arrow.get('2019-04-24T10:00:00.000-07:00'))  # 循ISO-8601的字符串不需要格式字符串参数即可转换
print(arrow.get('June was born in December 1994', 'MMMM YYYY'))  # 可以从字符串中通过格式参数搜索时间
print(arrow.get(2019, 4, 24))  # 直接创建arrow对象
print(arrow.Arrow(2019, 4, 24))  # 直接创建arrow对象

print('---------------------------')

'''arrow对象属性   datetime,timestamp,tzinfo'''
time_msg = arrow.now()
print(time_msg.datetime)
print(time_msg.timestamp)  # 时间戳
print(time_msg.naive)
print(time_msg.tzinfo)  # 时区
print(time_msg.hour)  # 小时
print(time_msg.day)  # 日期(天)

print('---------------------------')

'''时间推移    a.shift(**kwargs)'''
print(time_msg.shift(days=-1))  # 前一天
print(time_msg.shift(weeks=+1))  # 一周后
print(time_msg.shift(weekday=6))  # 距离time_msg最近的一个星期日，weekday从0到6代表周一到周日

print('---------------------------')

'''时间替换   a.replace(**kwargs)'''
print(time_msg.replace(hour=6))  # 将小时替换为6

print('---------------------------')

'''格式化输出    a.format([format_string])'''
print(time_msg.format())
print(time_msg.format('YYYY-MM-DD HH:mm:ss ZZ'))
