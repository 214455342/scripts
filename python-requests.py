# -*- coding:utf-8 -*-

import requests
import json


'''1.get请求'''
# 请求
r = requests.get('https://www.baidu.com')
# 传参
params_data = {'wd':'qiwenbao'}
r = requests.get('https://www.baidu.com', params=params_data)
print(r.url)  # 访问地址
print(r.text)  # 获取网页文本 返回的是Unicode型的数据   Unicode
print(r.content)  #获取网页文本 返回的是bytes型也就是二进制的数据。  str
# print(r.json()) # 如果获取的是json数据的话
print(r.status_code)  # 状态码
r = requests.get('https://www.baidu.com',stream=True)
print(r.raw)  # 返回原始socket respons，需要加参数stream=True
print(r.raw.read(10),'====')
print(r.cookies,'===')

'''2.POST请求'''
# 请求
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# 参数
data_msg = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=data_msg)
print(r.text)
print(r.cookies)

# 文件传递
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)

# session
# session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
s = requests.Session() #创建session对象
s.headers.update({'Content-Type': 'application/json'})
req_data = {"username": "admin", "password": "TYC123"}
r1 = s.post("http://172.24.115.208:8089/api/v1/user/login", data=json.dumps(req_data))
resp_data = r1.json()
token = resp_data.get('data').get('token') #获取token
print(token)
s.headers.update({'X-Token': token}) #更新token

r2 = s.get("http://172.24.115.208:8089/api/v1/canal/instances?name=&clusterServerId=&page=1&size=1000")
print(r.text,'==========')
