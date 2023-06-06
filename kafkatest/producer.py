# -*- coding: utf-8 -*-
import json

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'kafkatest'

for i in range(1000):
    producer.send(topic, json.dumps({
        'user': 'user_%d' % i,
    }).encode())

    print('send message %d' % i)
