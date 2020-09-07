# -*- coding: utf-8 -*-

###########################################################################
#                           装饰器                                        *
###########################################################################


import time
def timing(fn):
    def wrapper():
        start=time.time()
        fn()   #执行传入的fn参数
        stop=time.time()
        return (stop-start)
    return wrapper


@timing
def test_list_append():
    lst=[]
    for i in range(0,100000):
        lst.append(i)



@timing
def test_list_compre():
    lis = [i for i in range(0,100000)]  #列表生成式



a=test_list_append()
c=test_list_compre()
print("test list append time:",a)
print("test list comprehension time:",c)
print("append/compre:",round(a/c,3))
