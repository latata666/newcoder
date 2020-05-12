# -*- coding: utf-8 -*-
# @Time : 2020/5/12 11:00
# @Author : Mamamooo
# @Site :
# @File : ht_19.py
# @Software: PyCharm
"""
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。

"""

import sys

out = []
num ={}

while True:
    try:
        log_str = sys.stdin.readline()[:-1]
        #print(log_str)
        if log_str =="":
            break
        record,lines = log_str.split()
        #print(record,lines)
        if '\\' in record:
            name = record.split('\\')[-1][-16:]
            #rint(name)
        else:
            name = record[-16:]
            #print(name)
        item = name +' '+ lines
        if item not in num:
            num[item] = 1
            out.append(item)
        else:
            num[item] += 1
    except:
        break

for item in out[-8:]:
    sys.stdout.write(item + ' ' + str(num[item])+'\n')