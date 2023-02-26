import redis

redis_config = {
    'host': 'redis-testing',
    'port': 6379,
    'db': 1,
}

rs = redis.Redis(**redis_config)

if __name__ == '__main__':
    # INCR
    # 数值的递增
    rs.set('score', 88)
    rs.incr('score', 2)  # +2
    print(rs.get('score'))  # b'90'

    # INCRBY
    rs.incrby('score', 3)  # +3
    print(rs.get('score'))  # b'93'

    # INCRBYFLOAT
    rs.incrbyfloat('score', 0.5)  # +0.5
    print(rs.get('score'))  # b'93.5'

    # DESR
    # 数值的递减
    rs.set('score', 10)
    rs.decr('score', 1)
    print(rs.get('score'))  # b'9'

    # DESRBY
    rs.decrby('score', 3)
    print(rs.get('score'))  # b'6'
