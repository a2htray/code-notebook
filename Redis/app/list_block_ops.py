import redis
from threading import Thread

redis_config = {
    'host': 'redis-testing',
    'port': 6379,
    'db': 1,
}

rs = redis.Redis(**redis_config)


def lpush(key, *months):
    for month in months:
        rs.lpush(key, month)


def blpop(key, timeout):
    while True:
        ret = rs.blpop(key, timeout)
        if ret is None:
            break
        key, month = ret
        print(month)


if __name__ == '__main__':
    producer = Thread(target=lpush, args=('months', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    consumer = Thread(target=blpop, args=('months', 2))

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
