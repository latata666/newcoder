# -*- coding: utf-8 -*-
# @Time : 2020/7/3 14:06
# @Author : Mamamooo
# @Site :
# @File : py_jx_20_3_cp.py
# @Software: PyCharm
"""

"""

import asyncio
import random
import time

async def consumer(queue,id):
    while True:
        val = await queue.get()
        print('{} get a val: {}'.format(id,val))
        await asyncio.sleep(1)

async def producer(queue,id):
    for i in range(5):
        val = random.randint(1,10)
        await queue.put(val)
        print('{} put a val: {}'.format(id,val))
        await asyncio.sleep(1)

async def main():
    print("into main")
    queue = asyncio.Queue()

    consumer_1 = asyncio.create_task(consumer(queue, 'consumer_1'))
    consumer_2 = asyncio.create_task(consumer(queue, 'consumer_2'))

    producer_1 = asyncio.create_task(producer(queue, 'producer_1'))
    producer_2 = asyncio.create_task(producer(queue, 'producer_2'))

    print("create_task ok")


    await asyncio.sleep(10)
    consumer_1.cancel()
    consumer_2.cancel()

    time.sleep(10)
    await asyncio.gather(consumer_1,consumer_2,producer_1,producer_2,return_exceptions=True )

asyncio.run(main())


