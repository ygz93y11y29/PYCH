# -*- coding:utf-8 -*-
import redis

'''
    连结方式一：redis.Redis
        Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py
'''
r = redis.Redis(host='192.168.10.3',port='6379',password='123456',decode_responses=True,db='8')
r.set('foo', 'Bar')
print(r.get('foo'))

'''
    连结方式二：redis.StrictRedis：
        StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令。
'''
r = redis.StrictRedis(host='192.168.10.3',port='6379',password='123456',decode_responses=True,db='8')
r.set('foo1', 'Bar1')
print(r.get('foo'))
'''
    连结方式三：redis.ConnectionPool：
        StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令。
'''
pool = redis.ConnectionPool(host='192.168.10.3', port='6379',password='123456',decode_responses=True,db='8')
r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar')
print(r.get('foo'))

'''
    方法四
       
'''
redis_url = 'redis://root:xxxx@47.110.xx.xx:6379'
r = redis.Redis.from_url(redis_url,decode_responses=True) # 加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。
r.lpush('test_key','wwww')


