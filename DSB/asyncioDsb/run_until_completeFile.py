import asyncio
import datetime

async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()

#display_date(loop)协程运行完毕，run_until_complete才会返回，
# 否则阻塞。与之相似功能的call_soon却是不阻塞的。
loop.run_until_complete(display_date(loop))
print("stop")
loop.close()

