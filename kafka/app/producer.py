#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/6/7
import json

from kafka import KafkaProducer, KafkaClient

client = KafkaClient

producer = KafkaProducer(
    bootstrap_servers='127.0.0.1:9092',
    value_serializer=lambda d: json.dumps(d).encode('utf-8')
)

topic = 'test-topic'


def success(metadata):
    print(metadata.topic)


def error(exception):
    print(exception)


for i in range(5):
    data = {'id': i, 'name': 'name%d' % i}
    producer.send(topic=topic, value=data).add_callback(success).add_errback(error)

producer.flush()
producer.close()
