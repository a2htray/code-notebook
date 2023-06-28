#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/6/7

from kafka import KafkaConsumer

topic = 'test-topic'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers='127.0.0.1:9092',
    group_id='kafka-app',

    # auto_offset_reset='earliest',
)
print(consumer.topics())

for msg in consumer:
    print(msg)

