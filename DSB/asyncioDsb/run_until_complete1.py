# -*- coding:utf-8 -*-
import asyncio
import datetime

def hello_world(loop):
    print('Hello World')
    loop.stop()



def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        h = loop.call_later(1, display_date, end_time, loop)
        if (loop.time() + 3.0) > end_time:
            h.cancel()
            loop.stop()
    else:
        loop.stop()


loop = asyncio.get_event_loop()

# call_soon(callback),会把callback放到一个先进先出的队列，每个callback会被执行一次。
# call_soon注册的协程任务之后，立即返回，不阻塞，配合run_forever使用，run_forever会一直循环，直到loop.stop()。
# loop.call_soon(hello_world, loop)


end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()