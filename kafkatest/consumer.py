# -*- coding: utf-8 -*-

from kafka import KafkaConsumer

topic = 'kafkatest'

consumer = KafkaConsumer(topic, group_id='test_group2', bootstrap_servers='localhost:9092')

for msg in consumer:
    print(str(msg))
