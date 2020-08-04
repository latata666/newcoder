# -*- coding: utf-8 -*-
# @Time : 2020/7/1 15:07
# @Author : Mamamooo
# @Site :
# @File : func_t1.py
# @Software: PyCharm
"""

"""


# def func(d):
#     d['a'] = 10
#     d['b'] = 20
#
# d = {'a': 1, 'b': 2}
# func(d)
# print(d)


# def my_decorator(func):
#     def wrapper():
#         print('wrapper of decorator')
#         func()
#     return wrapper
#
# def greet():
#     print('hello world')
#
# greet = my_decorator(greet)
# greet()

#
# def my_decorator(func):
#     def wrapper():
#         print('wrapper of decorator')
#         func()
#     return wrapper
#
# @my_decorator
# def greet():
#     print('hello world')
#
# greet()


# def repeat(num):
#     def my_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 print('wrapper of decorator')
#                 func(*args, **kwargs)
#         return wrapper
#     return my_decorator
#
#
# @repeat(4)
# def greet(message):
#     print(message)
#
# greet('hello world')
#
#
# greet.__name__

# class Count:
#     def __init__(self, func):
#         self.func = func
#         self.num_calls = 0
#
#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print('num of calls is: {}'.format(self.num_calls))
#         return self.func(*args, **kwargs)
#
# @Count
# def example():
#     print("hello world")
#
# example()


import functools

def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)
    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)
    return wrapper


@my_decorator1
@my_decorator2
def greet(message):
    print(message)


greet('hello world')



