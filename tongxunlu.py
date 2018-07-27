#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import json


def message():
    if os.path.exists('tongxunlu'):
        if os.path.getsize('tongxunlu'):
            #print('文件存在且不为空')
            with open('tongxunlu','r+') as f:
                for line in f:
                    if line == '{}':
                        return 0
                    else:
                        return line
        else:
            #print('文件存在且为空')
            return 0
    else:
        #print('文件不存在')
        return 0

def zeng():
    dic1 = {}
    json_str = message()
    name = raw_input('请输入姓名：')
    phone = input("请输入号码：")
    if json_str == 0:
        dic1[name] = phone
        result = json.dumps(dic1)
    else:
        dic1 = json.loads(json_str)
        if dic1.get(name):
            print('已存在该联系人：%s' %name)
            exit(0)
        else:
            dic1[name] = phone
            result = json.dumps(dic1)
    with open('tongxunlu','w') as f:
        f.write(result)
    print(result)


def cha():
    dic1 = {}
    json_str = message()
    if json_str == 0:
        print("通讯录为空")
    else:
        name = raw_input('请输入姓名：')
        dic1 = json.loads(json_str)
        if dic1.get(name):
            v = dic1.get(name)
            print('号码是：%s' %v)
        else:
            print('无该联系人！')


def shan():
    dic1 = {}
    json_str = message()
    if json_str == 0:
        print("通讯录为空")
    else:
        name = raw_input('请输入姓名：')
        dic1 = json.loads(json_str)
        if dic1.get(name):
            dic1.pop(name)
            print('删除联系人：%s' %name)
            result = json.dumps(dic1)
            with open('tongxunlu', 'w') as f:
                f.write(result)
        else:
            print('无该联系人！')

def gai():
    dic1 = {}
    json_str = message()
    if json_str == 0:
        print("通讯录为空")
    else:
        name = raw_input('请输入姓名：')
        dic1 = json.loads(json_str)
        if dic1.get(name):
            phone = input('请输入号码：')
            dic1[name] = phone
            print('修改联系人：%s为%s' %(name, phone))
            result = json.dumps(dic1)
            with open('tongxunlu', 'w') as f:
                f.write(result)
        else:
            print('无该联系人！')

def index():
    v = input('请选择要执行的操作：\n 1.增\n 2.删\n 3.改\n 4.查 \n 请输入：')
    if v == 1:
        zeng()
    elif v == 2:
        shan()
    elif v == 3:
        gai()
    elif v == 4:
        cha()
    else:
        print('请输入正确的序号！')


index()