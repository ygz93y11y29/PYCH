import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main1():
    #create_task : 函数用来并发运行作为 asyncio 任务 的多个协程。
    task1 = asyncio.create_task(say_after(3, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")

    await task1
    await task2
    #await say_after(1, 'hello')

    print(f"finished at {time.strftime('%X')}")

'''
    可等待 对象有三种主要类型: 协程, 任务 和 Future.        
        
'''
async def nested():
    return 42

async def main2():
    '''
            Python 协程属于 可等待 对象，因此可以在其他协程中被等待:
    :return:
    '''
    print(await nested())  # will print "42".

async def main3():
    '''
        任务 被用来设置日程以便 并发 执行协程:
            当一个协程通过 asyncio.create_task() 等函数被打包为一个 任务，该协程将自动排入日程准备立即运行
    :return:
    '''
    task = asyncio.create_task(nested())
    print(await task)

async def main4():
    '''
        Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。
        当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。
        在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。
        通常情况下 没有必要 在应用层级的代码中创建 Future 对象。
        Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:
    :return:
    '''
    pass

async def main5():
    '''
    创建任务:
        asyncio.create_task(coro, *, name=None)
        将 coro 协程 打包为一个 Task 排入日程准备执行。返回 Task 对象。
        name 不为 None，它将使用 Task.set_name() 来设为任务的名称。
        该任务会在 get_running_loop() 返回的循环中执行，如果当前线程没有在运行的循环则会引发 RuntimeError。
        此函数 在 Python 3.7 中被加入。在 Python 3.7 之前，可以改用低层级的 asyncio.ensure_future() 函数。
    :return:
    '''
    pass

async def display_date():
    '''
    coroutine asyncio.sleep(delay, result=None, *, loop=None)
        阻塞 delay 指定的秒数。
        如果指定了 result，则当协程完成时将其返回给调用者。
        sleep() 总是会挂起当前任务，以允许其他任务运行。
        Deprecated since version 3.8, will be removed in version 3.10: loop 形参。
        以下协程示例运行 5 秒，每秒显示一次当前日期:
    :return:
    '''
    import datetime
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

'''
    并发运行任务
'''
async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main6():
    '''
    awaitable asyncio.gather(*aws, loop=None, return_exceptions=False)
        并发 运行 aws 序列中的 可等待对象。
        如果 aws 中的某个可等待对象为协程，它将自动作为一个任务加入日程。
        如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序
            与 aws 中可等待对象的顺序一致。
        如果 return_exceptions 为 False (默认)，所引发的首个异常会立即传播给等待 gather()
            的任务。aws 序列中的其他可等待对象 不会被取消 并将继续运行。
        如果 return_exceptions 为 True，异常会和成功的结果一样处理，并聚合至结果列表。
        如果 gather() 被取消，所有被提交 (尚未完成) 的可等待对象也会 被取消。
        如果 aws 序列中的任一 Task 或 Future 对象 被取消，它将被当作引发了 CancelledError 一
            样处理 -- 在此情况下 gather() 调用 不会 被取消。这是为了防止一个已提交的
            Task/Future 被取消导致其他 Tasks/Future 也被取消
            :return:
    '''
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

'''超时'''
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main7():
    '''
    coroutine asyncio.wait_for(aw, timeout, *, loop=None)
        等待 aw 可等待对象 完成，指定 timeout 秒数后超时。
        如果 aw 是一个协程，它将自动作为任务加入日程。
        timeout 可以为 None，也可以为 float 或 int 型数值表示的等待秒数。如果 timeout 为 None，则等待直到完成。
        如果发生超时，任务将取消并引发 asyncio.TimeoutError.
        要避免任务 取消，可以加上 shield()。
        函数将等待直到目标对象确实被取消，所以总等待时间可能超过 timeout 指定的秒数。
        如果等待被取消，则 aw 指定的对象也会被取消。
    :return:
    '''
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

'''来自其他线程的日程安排'''







if __name__ == '__main__':
    asyncio.run(main7())


