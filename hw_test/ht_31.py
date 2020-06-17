# -*- coding: utf-8 -*-
# @Time : 2020/6/10 17:43
# @Author : Mamamooo
# @Site :
# @File : ht_31.py
# @Software: PyCharm
"""
对字符串中的所有单词进行倒排。
说明：
1、构成单词的字符只有26个大写或小写英文字母；
2、非构成单词的字符均视为单词间隔符；
3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
4、每个单词最长20个字母；
输入描述:
输入一行以空格来分隔的句子

输出描述:
输出句子的逆序
示例1
输入
复制
I am a student
输出
复制
student a am I
"""

while True:
    try:
        s=input()
        for i in s:
            if not i.isalpha():
                s = s.replace(i,' ')
        temp=reversed(s.split())
        print(' '.join(temp))
    except:
        break



