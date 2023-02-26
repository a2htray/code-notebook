import redis

redis_config = {
    'host': 'redis-testing',
    'port': 6379,
    'db': 1,
}

rs = redis.Redis(**redis_config)

if __name__ == '__main__':
    # GETBIT
    # 取字符串指定位置的 bit 表示
    title = 'Redis with Python'
    for c in title:
        print(bin(ord(c)))

    # 0b1010010
    # 0b1100101
    # 0b1100100
    # 0b1101001
    # 0b1110011
    # 0b100000
    # 0b1110111
    # 0b1101001
    # 0b1110100
    # 0b1101000
    # 0b100000
    # 0b1010000
    # 0b1111001
    # 0b1110100
    # 0b1101000
    # 0b1101111
    # 0b1101110

    rs.set('title', title)

    print(rs.getbit('title', 0))  # 0
    print(rs.getbit('title', 1))  # 1
    print(rs.getbit('title', 2))  # 0
    print(rs.getbit('title', 3))  # 1
    print(rs.getbit('title', 4))  # 0
    print(rs.getbit('title', 5))  # 0
    print(rs.getbit('title', 6))  # 1
    print(rs.getbit('title', 7))  # 0

    # SETBIT
    # 设置指定位置上的二进制值
    rs.setbit('title', 8 * 15 - 1, 1)  # Python 中 h 变成了 i
    print(rs.get('title'))  # b'Redis with Pytion'

    # BITCOUNT
    # 返回字符串的二进制表示中 1 的个数
    print(rs.bitcount('title', 0, 8 * 15))  # 64

    # BITOP
    # 对多个键执行位运算
    can_view = 0b0001
    can_add = 0b0010
    can_delete = 0b0100
    can_cancel = 0b1000

    rs.set('can_view', can_view)
    rs.set('can_add', can_add)
    rs.set('can_delete', can_delete)
    rs.set('can_cancel', can_cancel)

    rs.bitop('OR', 'permission', 'can_view', 'can_delete')  # 设置权限：可看、可删除
    permission = int(rs.get('permission'))
    print(
        permission,  # 5
        permission & can_view,  # 判断是否有"可看"的权限，输出 1
        permission & can_cancel,  # 判断是否有"可删除"的权限，输出 0
    )

    # BITPOS
    # 获取字符串表示的二进制中第一个为 0 或 1 的位置
    print(rs.bitpos('permission', 1))  # 2
