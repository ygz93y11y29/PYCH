# -*- coding:utf-8 -*-
import datetime
import time

# 1.时间日期转时间戳
now = datetime.datetime.now()#datatime类型
time_stamp = time.mktime(now.timetuple())
print(int(time_stamp))#秒级

# 2.时间字符串转时间戳
st = time.strptime('2018-10-07 16:12:54', '%Y-%m-%d %H:%M:%S')
time_stamp = time.mktime(st)
print(int(time_stamp))#秒级

# 3.直接生成当前时间戳
import time
time_stamp = int(time.time())
print(time_stamp)#int

# 4.时间戳转时间字符串
ltime = time.localtime(1552723974)
time_stamp  = time.strftime('%Y-%m-%d %H:%M:%S',ltime)
print(time_stamp)#str



