# -*- coding: utf-8 -*-
# @Time : 2020/5/18 14:34
# @Author : Mamamooo
# @Site :
# @File : scmetho.py
# @Software: PyCharm
"""

"""


class test:
    class_name = "test"

    def __init__(self, name):
        self.class_name = name

    def my_print(self, value):
        print(value + " " + self.class_name)

    @staticmethod
    def my_static_print(val):
        print(val)

    @classmethod
    def my_class_print(cls, val):
        print(val + " " + cls.class_name)


if __name__ == "__main__":
    my_test = test("xxx")

    test.my_static_print("static print")
    test.my_class_print("class print")
    my_test.my_static_print("static print")
    my_test.my_class_print("class print")
    my_test.my_print("my_print")