import pymysql
import re
import csv
import requests
import json


def canal_csv():
    conn = pymysql.connect(
        host='rm-2zet04367c01q5e0j.mysql.rds.aliyuncs.com',
        user='jindi', password='J1ndiCanal',
        database='canal_manager',
        charset='utf8')

    cursor = conn.cursor()
    sql = 'select canal_instance_config.name,canal_instance_config.status,canal_instance_config.content,canal_instance_config.modified_time,canal_cluster.name,canal_cluster.zk_hosts,canal_instance_config.id \
        from canal_instance_config inner join canal_cluster on canal_instance_config.cluster_id = canal_cluster.id'
    cursor.execute(sql)
    results = cursor.fetchall()
    f = open('canal_instance.csv', 'w', encoding='utf-8', newline='' "")
    csv_writer = csv.writer(f)
    csv_writer.writerow(["实例id", "实例名", "运行状态", "监听rds", "监听库表", "修改时间", "所在集群", "topic", "topic是否有数据"])
    for res in results:
        content = res[2]
        pattern_rds = "canal.instance.master.address=(.*):3306"
        pattern_table = "canal.instance.filter.regex=(.*)\n"
        pattern_dynamic = "#canal.mq.dynamicTopic=(.*)\n"
        mach_rds = re.search(pattern_rds, content)
        rds = (mach_rds.group(1)) #instance rds addr
        mach_table = re.search(pattern_table, content)
        tables = mach_table.group(1) #instance db.table
        mach_dynamic = re.search(pattern_dynamic, content)
        for table in tables.split(','):
            if mach_dynamic is None:
                topic = table
            else:
                topic = "canal-default"
            name = res[0]
            status = res[1]
            modified_time = res[3]
            cluster_name = res[4]
            cluster_zk = res[5]
            id = res[6]
            data = prometheus(cluster_name, topic)
            # print(id, name, status, rds, table, modified_time, cluster_name, cluster_zk, topic)
            csv_writer.writerow([id, name, status, rds, table, modified_time, cluster_name, topic, data])

    f.close()
    cursor.close()
    conn.close()


def prometheus(cluster,topic):
    start = '2021-08-10T20:10:51.781Z'
    end = '2021-08-17T20:10:51.781Z'
    step = '6h'
    if cluster == 'ToKafka':
        cluster = 'canal-kafka'
    if cluster == 'ToKafkaProd2':
        cluster = 'canal-kafka-prod2'
    if cluster == 'PreRelease':
        cluster = 'canal-pre'
    if cluster == 'TestRelease':
        cluster = 'canal-test'
    query = "sum(delta(kafka_topic_partition_current_offset{cluster=~'%s', topic=~'%s'}[5m])/5) by (topic)" %(cluster, topic)
    print(f'http://172.24.115.201:9090/api/v1/query_range?query={query}&start={start}&end={end}&step={step}')
    req = requests.get(f'http://172.24.115.201:9090/api/v1/query_range?query={query}&start={start}&end={end}&step={step}')
    datas = (json.loads(req.text))
    if not datas['data']['result']:
        print(datas)
        return 0
    data_list = (datas['data']['result'][0]['values'])
    new_list = []
    for i in data_list:
        new_list.append(i[1])
    x = float(max(new_list))
    if x > 0:
        return 1
    else:
        return 0


canal_csv()
