import redis

redis_config = {
    'host': 'redis-testing',
    'port': 6379,
    'db': 1,
}

rs = redis.Redis(**redis_config)


if __name__ == '__main__':
    # LPUSH
    # 创建 colors，并向左添加两个元素
    # 返回添加后列表的长度
    print(rs.lpush('colors', 'green', 'yellow'))  # 2

    # LPUSHX
    # 向 colors 添加新的元素
    # 返回添加后列表的长度
    print(rs.lpushx('colors', 'red'))  # 3

    # LPUSHX
    # 向不存在的列表添加元素，不会创建相应列表并返回 0
    print(rs.lpushx('notExistColors', 'green'))  # 0

    # RPUSH
    # 向右添加一个元素
    # 返回添加后列表的长度
    print(rs.rpush('colors', 'gray'))  # 4

    # RPUSHX
    # 向右添加一个元素
    # 返回添加后列表的长度
    print(rs.rpushx('colors', 'orange'))  # 5

    # RPUSHX
    # 向不存在的列表添加元素，不会创建相应列表并返回 0
    print(rs.rpushx('notExistColors', 'green'))  # 0

    # LPOP
    # 取列表左边的第一个元素并从列表中移除该元素
    print(rs.lpop('colors'))  # b'red'

    # RPOP
    # 取列表右边的第一个元素并从列表中移除该元素
    color = rs.rpop('colors')
    print(color)  # b'orange'

    # LLEN
    # 获取列表中元素的个数
    # 如果指定列表不存在，返回 0
    print(rs.llen('colors'))  # 3
    print(rs.llen('notExistColors'))  # 0

    # LRANGE
    # 取列表中指定区间内连续的子集

    # 取全部
    print(rs.lrange('colors', 0, -1))  # [b'yellow', b'green', b'gray']
    # 取闭区间 [0, 1] 的元素
    print(rs.lrange('colors', 0, 1))  # [b'yellow', b'green']

    # LREM
    # 从左端删除指定个数的元素
    # 第三个参数指定要删除的值
    # 返回被删除元素的个数
    print(rs.lrem('colors', 2, 'green'))  # 1

    # LINDEX
    # 取指定位置上的元素
    print(rs.lindex('colors', 0))  # b'yellow'
    # 超过列表索引最大值返回 None
    print(rs.lindex('colors', 3))  # None

    # LSET
    # 设置指定位置的值
    # 返回是否设置成功
    print(rs.lset('colors', 0, 'red'))  # True

    # LTRIM
    # 截取原列表并保存至原列表
    # 返回是否截取成功
    print(rs.ltrim('colors', 0, 0))  # True

    # LINSERT
    # 在指定元素前或后插入元素
    # 返回插入成功后的列表长度
    print(rs.linsert('colors', 'AFTER', 'red', 'green'))  # 2
    # 向不存在的列表插入元素返回 0
    print(rs.linsert('notExistColors', 'BEFORE', 'red', 'green'))  # 0

    # RPOPLPUSH
    # 操作两个列表，从一个列表右端弹出元素并向左端添加到另一个列表
    # 返回被操作的元素
    rs.lpush('otherColors', 'yellow')
    print(rs.rpoplpush('colors', 'otherColors'))  # b'green'

    rs.delete('colors')
    rs.delete('otherColors')
