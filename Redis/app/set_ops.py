import redis

redis_config = {
    'host': 'redis-testing',
    'port': 6379,
    'db': 1,
}

rs = redis.Redis(**redis_config)

if __name__ == '__main__':
    rs.sadd('projectA', *['A001', 'A002', 'A003'])
    rs.sadd('projectAB', *['A001', 'A002', 'A003', 'B001', 'B002'])

    # SDIFF
    # 取集合的差集
    # 若参数为 S1, S2, S3, ...，则返回结果为 S1 - S2 - S3 - ...
    print(rs.sdiff('projectA', 'projectAB'))  # set()
    print(rs.sdiff('projectAB', 'projectA'))  # {b'B001', b'B002'}

    # SINTER
    # 取集合的交集
    print(rs.sinter('projectA', 'projectAB'))  # {b'A001', b'A003', b'A002'}

    # SUNION
    # 取集合的并集
    rs.sadd('projectB', *['B001', 'B002'])
    print(rs.sunion('projectA', 'projectB'))  # {b'A002', b'A001', b'B001', b'A003', b'B002'}

    # SDIFFSTORE
    # 计算集合的差集并将结果保存至另一键的集合中
    # 返回差集中元素的个数
    rs.delete('projectB')
    print(rs.sdiffstore('projectB', 'projectAB', 'projectA'))  # 2
    print(rs.smembers('projectB'))  # {b'B001', b'B002'}

    # SINTERSTORE
    # 计算集合的交集并将结果保存至另一键的集合中
    # 返回交集中元素的个数
    print(rs.sinterstore('newProjectB', 'projectAB', 'projectB'))  # 2
    print(rs.smembers('newProjectB'))  # {b'B001', b'B002'}

    # SUNIONSTORE
    # 计算集合的并集并将结果保存至另一键的集合中
    # 返回并集中元素的个数
    rs.delete('projectAB')
    print(rs.sunionstore('projectAB', 'projectA', 'projectB'))  # 5
    print(rs.smembers('projectAB'))  # {b'A002', b'A001', b'B001', b'A003', b'B002'}
