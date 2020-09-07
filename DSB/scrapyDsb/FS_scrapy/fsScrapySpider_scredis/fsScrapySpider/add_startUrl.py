# -*- coding: utf-8 -*-
import redis
import time

conn = redis.Redis(host='192.168.10.3',port='6379',password='123456',decode_responses=True,db='15')

qwpyBaseUrl = 'http://qc.wa.news.cn/nodeart/list?nid=11148362&pgnum={}&cnt=10&tp=1&orderby=1?callback=jQuery112405951037093341978_1592276347200&_={}'
zzsBaseUrl =  'http://qc.wa.news.cn/nodeart/list?nid=11148367&pgnum={}&cnt=10&tp=1&orderby=1?callback=jQuery1124016917371617397858_1592285480616&_={}'
for i in range(1, 4):
    timeStr = int(time.time() * 1000)
    qwpyUrl = qwpyBaseUrl.format(i, timeStr, timeStr+1)
    conn.lpush('sppySpider:start_urls', qwpyUrl)
    zzsUrl = zzsBaseUrl.format(i, timeStr, timeStr)
    conn.lpush('sppySpider:start_urls', zzsUrl)


print(conn.lrange('sppySpider:start_urls', 0, 50))
conn.close()