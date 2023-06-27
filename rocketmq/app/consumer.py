# -*- coding: utf-8 -*-
import time
import json
from rocketmq.client import PushConsumer


def callback(msg):
    data = json.loads(msg.body)
    print(data)


consumer = PushConsumer('PID-XXX')
consumer.set_namesrv_addr('rmqnamesrv:9876')
consumer.subscribe('rocketmq-test', callback)
consumer.start()

while True:
    time.sleep(10)

# consumer.shutdown()
