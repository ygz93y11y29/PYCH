# -*- coding: utf-8 -*-
import datetime
import time
import calendar
##############################################################################
#                        time       datetime                                 #
##############################################################################

t = time.time()
print("time.time:   ",t)

#---------------------------------------------------------------------------------将时间戳转换为struct_time
gmtime = time.gmtime(t)
print('time.gmtime: ', gmtime)
localtime = time.localtime(t)
print('time.localtime:  ', localtime)
#---------------------------------------------------------------------------------将struct_time转换为时间戳
print("calendar.timegm: ", calendar.timegm(gmtime))
print("time.mktime: ", time.mktime(localtime))

'''
    strftime 即 string format time，用来将时间格式化成字符串
    strptime 即string parse time，用来将字符串解析成时间。
'''
#---------------------------------------------------------------------------------将时间戳转换为字符串
print("time.strftime:   ", time.strftime('%Y %m %d  %H %M %S', time.gmtime()))
#---------------------------------------------------------------------------------将字符串转换为struct_time
print("time.strptime:   ", time.strptime('2020 07 17  06 57 06', '%Y %m %d  %H %M %S', ))

####################################################################################
#-----------------------------------------------------------------------------------获取当前时间
print("datetime.datetime.now(): ", datetime.datetime.now())
print("datetime.datetime.today():   ", datetime.datetime.today())






