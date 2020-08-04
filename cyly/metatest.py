# -*- coding: utf-8 -*-
# @Time : 2020/7/1 16:52
# @Author : Mamamooo
# @Site :
# @File : metatest.py
# @Software: PyCharm
"""

"""
import yaml

# class Monster(yaml.YAMLObject):
#   yaml_tag = u'!Monster'
#   def __init__(self, name, hp, ac, attacks):
#     self.name = name
#     self.hp = hp
#     self.ac = ac
#     self.attacks = attacks
#   def __repr__(self):
#     return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
#        self.__class__.__name__, self.name, self.hp, self.ac,
#        self.attacks)
#
# yaml.load("""
# --- !Monster
# name: Cave spider
# hp: [2,6]    # 2d6
# ac: 16
# attacks: [BITE, HURT]
# """)
#
# Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])
#
# print (yaml.dump(Monster(
#     name='Cave lizard', hp=[3,6], ac=16, attacks=['BITE','HURT'])))


class Mymeta(type):
    def __init__(self, name, bases, dic):
        super().__init__(name, bases, dic)
        print('===>Mymeta.__init__')
        print(self.__name__)
        print(dic)
        print(self.yaml_tag)

    def __new__(cls, *args, **kwargs):
        print('===>Mymeta.__new__')
        print(cls.__name__)
        return type.__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('===>Mymeta.__call__')
        obj = cls.__new__(cls)
        cls.__init__(cls, *args, **kwargs)
        return obj


class Foo(metaclass=Mymeta):
    yaml_tag = '!Foo'

    def __init__(self, name):
        print('Foo.__init__')
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('Foo.__new__')
        return object.__new__(cls)


foo = Foo('foo')
