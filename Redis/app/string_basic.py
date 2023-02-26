import time
import redis

redis_config = {
    'host': 'redis-testing',
    'port': 6379,
    'db': 1,
}

rs = redis.Redis(**redis_config)

if __name__ == '__main__':
    # SET
    # 设置单个键值对
    # 返回是否设置成功
    print(rs.set('name', 'a2htray'))  # True

    # SETNX
    # 设置单个键值对，只有当键不存在时有效
    print(rs.setnx('name', 'a2htray2'))  # False
    print(rs.setnx('notExistName', 'a2htray'))  # True

    # SETEX
    # 设置具有生存时间的键值对，单位为秒
    print(rs.setex('course', 1, 'math'))  # True
    time.sleep(1.5)  # 设置 1.5 秒后访问
    print(rs.get('course'))  # None

    # PSETEX
    # 设置具有生存时间的键值对，单位为微秒
    # 1000 微秒 = 1 秒
    print(rs.psetex('store', 1000, '59'))  # True
    time.sleep(1.5)
    print(rs.get('store'))  # None

    # GET
    # 获取值
    print(rs.get('name'))  # b'a2htray'

    # GETSET
    # 设置值并返回旧值，若旧值不存在返回 None
    print(rs.getset('name', 'jimmy'))  # b'a2htray'
    print(rs.getset('otherName', 'Tonny'))  # None

    # GETRANGE
    # 根据给定的索引区间，以闭区间的方式返回字符串的子串
    # 若指定的 key 不存在，则返回空字符串
    print(rs.getrange('name', 0, 2))  # b'jim'
    print(rs.getrange('notExistName2', 0, 2))  # b''

    # SETRANGE
    # 根据给定的索引和值，原字符串中从该索引位置起用值进行替换
    # 返回新字符串的长度
    print(rs.setrange('name', 1, 'xxx'))  # 5
    print(rs.setrange('name', 4, 'xxx'))  # 7

    # MSET
    # 同时设置多个键值对
    print(rs.mset({'width': 10, 'height': 20}))

    # MSETNX
    # 设置多个键值对，若某个键存在，其余键值设置不会生效
    # 由于 width 已存在，所以 objName 设置末生效
    print(rs.msetnx({'width': 20, 'objName': 'AD00001'}))  # False

    # MGET
    # 同时取多个值
    print(rs.mget('width', 'height'))  # [b'10', b'20']

    # STRLEN
    # 取字符串长度
    print(rs.strlen('name'))  # 7

    # APPEND
    # 追回字符串，返回追加后字符串的长度
    print(rs.append('name', '0001'))  # 11
    # 若指定的键不存在，则会先创建一个值为空的键，并在其后进行追回
    print(rs.append('anotherName', 'Ann'))  # 3