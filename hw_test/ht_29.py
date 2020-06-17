# -*- coding: utf-8 -*-
# @Time : 2020/6/8 13:19
# @Author : Mamamooo
# @Site :
# @File : ht_29.py
# @Software: PyCharm
"""
1、对输入的字符串进行加解密，并输出。
2加密方法为
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
3、解密方法为加密的逆过程。
"""

def Encrypt(char):
    if char.isdigit():
        print(str(int(char) + 1))
        return str(int(char) + 1)[-1]
    else:
        if char.lower() == 'z':
            return 'a' if char == 'Z' else 'A'
        else:
            ch = chr(ord(char) + 1)
            return ch.lower() if char.isupper() else ch.upper()

def unEncrypt(char):
    if char.isdigit():
        return str(int(char) - 1) if int(char) > 0 else str(9)
    else:
        if char == 'a' or char == 'A':
            return 'Z' if char == 'a' else 'z'
        else:
            ch = chr(ord(char) - 1)
            return ch.lower() if char.isupper() else ch.upper()

while True:
    try:
        en = input()
        de = input()
        re1 = []
        re2 = []
        for x in en:
            if x.isdigit() or x.isalpha():
                re1.append(Encrypt(x))
            else:
                re1.append(x)
        for x in de:
            if x.isdigit() or x.isalpha():
                re2.append(unEncrypt(x))
            else:
                re2.append(x)

        print(''.join(re1))
        print(''.join(re2))
    except:
        break


