import redis

redis_config = {
    'host': 'redis-testing',
    'port': 6379,
    'db': 1,
}

rs = redis.Redis(**redis_config)


def server_state():
    if rs.ping():
        print('redis server running ...')
    else:
        print('redis server unreachable')


def key_exists(key):
    if rs.exists(key):
        print(f'key: {key} exists')
    else:
        print(f'key: {key} does not exist')


def list_test():
    values = [1, 2, 3, 4]
    n = rs.lpush('testListKey', *values)
    print('create a list with values [{values}] and length {n}'.format(
        values=', '.join([str(v) for v in values]),
        n=n,
    ))
    delete_key('testListKey')


def delete_key(key):
    rs.delete(key)


if __name__ == '__main__':
    server_state()
    key_exists('keyNotExist')
    list_test()
