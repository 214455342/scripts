import requests
import json
import re
import xlwt

s = requests.Session()
s.headers.update({'Content-Type': 'application/json'})
req_data = {"username": "admin", "password": "TYC123"}
r1 = s.post("http://172.24.115.208:8089/api/v1/user/login", data=json.dumps(req_data))
resp_data = r1.json()
token = resp_data.get('data').get('token')
print(token)
s.headers.update({'X-Token': token})
r2 = s.get("http://172.24.115.208:8089/api/v1/canal/instances?name=&clusterServerId=&page=1&size=1000")
resp2_data = r2.json()
instances_li = []
for i in resp2_data.get('data').get('items'):
    tmp_dict = {}
    tmp_dict["name"] = i["name"]
    tmp_dict["running"] = i["runningStatus"]
    tmp_dict["id"] = i["id"]
    tmp_dict["clusterId"] = i["clusterId"]
    instances_li.append(tmp_dict)
instances_li = [i for i in instances_li if i["running"] == "1"]
#print(instances_li)
# instances_li = [i for i in instances_li if i["clusterId"] == 1 or i["clusterId"] == 9]
instances_li = [i for i in instances_li if i["clusterId"] == 9]
#print(instances_li)


def instance_config(instances_id):
    r3 = s.get(f"http://172.24.115.208:8089/api/v1/canal/instance/{instances_id}")
    resp3_data = r3.json()
    # print(resp3_data)
    instance_content = resp3_data.get("data").get("content")
    matchObj = re.search('\\ncanal.instance.filter.regex=(.*)\\n', instance_content)
    #print(matchObj.group(1))
    topic_li = matchObj.group(1).strip().split(",")
    return topic_li


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = bold
    font.bold = bold
    font.colour_index = 4
    font.height = height
    font.name = name
    style.font = font
    return style


for i in instances_li:
    topic_li = instance_config(i["id"])
    i["topic_li"] = topic_li
print(instances_li)

def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 添加表格 sheet1
    row0 = [u'instances_id', u'topic']
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style("Time New Roman", 220, True))  # 第一行数据写入
    stop_hang = 0
    for i in instances_li:
        tmp_hang = len(i["topic_li"])
        start_hang, stop_hang = stop_hang + 1, stop_hang + tmp_hang
        sheet1.write_merge(start_hang, stop_hang, 0, 0, i["name"])  # 合并那几个单元格,行_start,行_stop,列_start,列_stop
    stop_hang = 0
    for i in instances_li:
        for i, j in enumerate(i["topic_li"]):
            stop_hang = stop_hang + 1
            sheet1.write(stop_hang, 1, j)

    f.save('topic.xls')


if __name__ == '__main__':
    write_excel()
for i in instances_li:
    for j in i["topic_li"]:
        print(f"http://172.24.115.219:3000/d/jwPKIsniz/kafkaji-qun-jian-kong?orgId=1&from=now-5m&to=now&var-job=kafka_exporter&var-clustername=canal-kafka-prod2&var-topic={j}&var-consumergroup=")
