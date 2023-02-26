import redis

redis_config = {
    'host': 'redis-testing',
    'port': 6379,
    'db': 1,
}

rs = redis.Redis(**redis_config)

if __name__ == '__main__':
    # SADD 向集合中添加元素
    # 返回添加成功元素的个数
    print(rs.sadd('numbers', 1, 2, 3, 4, 5))  # 5
    # 由于 4, 5 已存在于 numbers 集合，所以只需要添加 6, 7, 8，返回成功添加的个数 3
    print(rs.sadd('numbers', 4, 5, 6, 7, 8))  # 3

    # SREM
    # 删除集合中的元素，返回成功删除的元素个数
    print(rs.srem('numbers', *[1, 2, 3]))  # 3
    print(rs.srem('numbers', *[1, 2, 3, 4]))  # 1

    # SMEMBERS
    # 获取集合中的所有元素，返回类型对应 Python 中的 set 类型
    print(rs.sadd('alphabet', *['a', 'b', 'c']))  # 3
    print(rs.smembers('alphabet'))  # {b'b', b'a', b'c'}

    # SCARD
    # 取集合中元素的个数
    print(rs.scard('alphabet'))  # 3

    # SRANDMEMBER
    # 随机取集合中指定个数的元素
    # 随机输出，结果不保证一致
    print(rs.srandmember('alphabet', 1))  # [b'b']
    # 指定个数大于集合元素个数时，返回全部元素
    print(rs.srandmember('alphabet', 4))  # [b'c', b'a', b'b']

    # SPOP
    # 从集合中弹出指定个数的元素
    print(rs.spop('alphabet', 2))  # [b'b', b'c']
    print(rs.smembers('alphabet'))  # {b'a'}
