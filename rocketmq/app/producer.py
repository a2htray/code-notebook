# -*- coding: utf-8 -*-
import json

from rocketmq.client import Producer, Message

producer = Producer('PID-XXX')
producer.set_namesrv_addr('rmqnamesrv:9876')
producer.start()

for i in range(10):
    msg = Message('rocketmq-test')
    msg.set_keys('key%d' % i)
    msg.set_tags('tag%d' % i)
    msg.set_body(json.dumps({
        'user': 'user%d' % i,
    }))
    ret = producer.send_sync(msg)
    print(ret.status, ret.msg_id, ret.offset)

producer.shutdown()
