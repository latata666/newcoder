# -*- coding: utf-8 -*-
# @Time : 2020/7/3 13:32
# @Author : Mamamooo
# @Site :
# @File : py_jx_20_2.py
# @Software: PyCharm
"""

"""

# import asyncio
#
# async def worker_1():
#     print('worker_1 start')
#     await asyncio.sleep(1)
#     print('worker_1 done')
#
# async def worker_2():
#     print('worker_2 start')
#     await asyncio.sleep(2)
#     print('worker_2 done')
#
# async def main():
#     print('before await')
#     await worker_1()
#     print('awaited worker_1')
#     await worker_2()
#     print('awaited worker_2')
#
# asyncio.run(main())
#


# import asyncio
#
# async def worker_1():
#     print('worker_1 start')
#     await asyncio.sleep(1)
#     print('worker_1 done')
#
# async def worker_2():
#     print('worker_2 start')
#     await asyncio.sleep(2)
#     print('worker_2 done')
#
# async def main():
#     task1 = asyncio.create_task(worker_1())
#     task2 = asyncio.create_task(worker_2())
#     print('before await')
#     await task1
#     print('awaited worker_1')
#     await task2
#     print('awaited worker_2')
#
# asyncio.run(main())


import asyncio

async def worker_1():
    await asyncio.sleep(1)
    return 1

async def worker_2():
    await asyncio.sleep(2)
    return 2 / 0

async def worker_3():
    await asyncio.sleep(3)
    return 3

async def main():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    await asyncio.sleep(2)
    task_3.cancel()

    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)

asyncio.run(main())



