# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # author: a2htray
# # create date: 2023/6/26
import json

from rocketmq.client import Producer, Message

producer = Producer('PID-001')
producer.set_namesrv_addr('localhost:9876')
producer.start()

for i in range(10):
    msg = Message('TEST-TOPIC')
    msg.set_body(json.dumps({
        'no': i,
    }))

    ret = producer.send_sync(msg)
    print(ret)

print('end')
