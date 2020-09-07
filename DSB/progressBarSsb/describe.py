# -*- coding: utf-8 -*-
import sys
import time
##############################################################################
#                                进度条                                      #
##############################################################################

#-----------------------------------------------------------------------------第一种
def progress_bar():
    for i in range(1, 101):
        print("\r", end="")
        print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
        time.sleep(0.05)
progress_bar()
#-----------------------------------------------------------------------------第二种
scale = 50
print("执行开始，祈祷不报错".center(scale // 2,"-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
    time.sleep(0.1)
print("\n"+"执行结束，万幸".center(scale // 2,"-"))
#-----------------------------------------------------------------------------第三种
from time import sleep
from tqdm import tqdm
# 这里同样的，tqdm就是这个进度条最常用的一个方法
# 里面存一个可迭代对象
for i in tqdm(range(1, 500)):
   # 模拟你的任务
   sleep(0.01)
sleep(0.5)

#-----------------------------------------------------------------------------第四种
import time
from progress.bar import IncrementalBar
mylist = [1,2,3,4,5,6,7,8]
bar = IncrementalBar('Countdown', max = len(mylist))
for item in mylist:
    bar.next()
    time.sleep(1)
    bar.finish()
#-----------------------------------------------------------------------------第五种
from alive_progress import alive_bar
items = range(100)                  # retrieve your set of items
with alive_bar(len(items)) as bar:   # declare your expected total
    for item in items:               # iterate as usual
        # process each item
        bar()
        time.sleep(0.1)
#-----------------------------------------------------------------------------第六种
import PySimpleGUI as sg
import time
mylist = [1,2,3,4,5,6,7,8]
for i, item in enumerate(mylist):
    sg.one_line_progress_meter('This is my progress meter!', i+1, len(mylist), '-key-')
    time.sleep(1)

