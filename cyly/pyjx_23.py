# # -*- coding: utf-8 -*-
# # @Time : 2020/7/3 16:48
# # @Author : Mamamooo
# # @Site :
# # @File : pyjx_23.py
# # @Software: PyCharm
# """
#
# """
#
#
# # from threading import Thread
# #
# #
# # def CountDown(n):
# #     while n > 0:
# #         n -= 1
# #
# # n = 100000000
# #
# # t1 = Thread(target=CountDown, args=[n // 2])
# # t2 = Thread(target=CountDown, args=[n // 2])
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
#
#
# import threading
#
# n = 0
#
# def foo():
#     global n
#     n += 1
#
# threads = []
# for i in range(100):
#     t = threading.Thread(target=foo)
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()
#
# print(n)


import os
import psutil


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

show_memory_info(1)

assert 1 == 2, 'This should fail'