# -*- coding: utf-8 -*-
# @Time : 2020/7/3 9:41
# @Author : Mamamooo
# @Site :
# @File : py_jx_20_1.py
# @Software: PyCharm
"""

"""


# import time
# import asyncio
#
# async def crawl_page(url):
#         print('crawling {}'.format(url))
#         sleep_time = int(url.split('_')[-1])
#         await  asyncio.sleep(sleep_time)
#         print('OK {}'.format(url))
#
#
# async def main(urls):
#         for url in urls:
#             await crawl_page(url)
#
# asyncio.run(
# main(['url_1', 'url_2', 'url_3', 'url_4'])
# )


import asyncio

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
