from kafka import KafkaConsumer


def start_consumer():
    consumer = KafkaConsumer('liuguangcheng.user_college', bootstrap_servers='10.2.16.38:9092')
    for msg in consumer:
        # print('接收到的信息为：',msg)
        print("转换后的value：", msg.value.decode())


start_consumer()
