# -*- coding: utf-8 -*-
# @Time : 2020/5/13 20:38
# @Author : Mamamooo
# @Site :
# @File : ht_21.py
# @Software: PyCharm
"""
简单密码破解
输入描述:
输入包括多个测试数据。输入是一个明文，密码长度不超过100个字符，输入直到文件结尾
输出描述:
输出渊子真正的密文
"""

while True:
    try:
        pwd = input()
        new = ''

        for s in pwd:
            if s.isupper():
                if s == 'Z':
                    new += 'a'
                else:
                    new += chr(ord(s.lower()) +1 )
            elif s.islower():
                if s in 'abc':
                    new += '2'
                elif s in 'def':
                    new += '3'
                elif s in 'ghi':
                    new += '4'
                elif s in 'jkl':
                    new += '5'
                elif s in 'mno':
                    new += '6'
                elif s in 'pqrs':
                    new += '7'
                elif s in 'tuv':
                    new += '8'
                elif s in 'wxyz':
                    new += '9'
            elif s.isdigit():
                    new += s
        print(new.strip())
    except:
        break