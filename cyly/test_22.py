# -*- coding: utf-8 -*-
# @Time : 2020/7/1 17:24
# @Author : Mamamooo
# @Site :
# @File : test_22.py
# @Software: PyCharm
"""

"""

import os
import psutil


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')

def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')

print( test_iterator())
print( test_generator())






















# def generator(k):
#     i = 1
#     while True:
#         yield i ** k
#         i += 1
#
# gen_1 = generator(1)
# gen_3 = generator(3)
# print(gen_1)
# print(gen_3)
#
# def get_sum(n):
#     sum_1, sum_3 = 0, 0
#     for i in range(n):
#         next_1 = next(gen_1)
#         next_3 = next(gen_3)
#         print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
#         sum_1 += next_1
#         sum_3 += next_3
#     print(sum_1 * sum_1, sum_3)
#
# get_sum(8)

