#encoding:utf8
from pykafka import KafkaClient
client = KafkaClient(hosts="172.26.123.237:9092")
topic = client.topics['search_eval.eval_query']
# 获取 consumer 消费者
consumer = topic.get_simple_consumer(consumer_group="test",reset_offset_on_start=True)
for message in consumer:
    if message is not None:
        print(">>>>>>>>>>", message.offset, message.value.decode())
