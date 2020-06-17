# -*- coding: utf-8 -*-
# @Time : 2020/6/10 15:08
# @Author : Mamamooo
# @Site :
# @File : ht_30.py
# @Software: PyCharm

"""
详细描述：
将输入的两个字符串合并。
对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标意思是字符在字符串中的位置。
对排序后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，则对他们所代表的16进制的数进行BIT倒序的操作，
并转换为相应的大写字符。如字符为‘4’，为0100b，则翻转后为0010b，也就是2。转换后的字符为‘2’； 如字符为‘7’，为0111b，
则翻转后为1110b，也就是e。转换后的字符为大写‘E’。
举例：输入str1为"dec"，str2为"fab"，合并为“decfab”，分别对“dca”和“efb”进行排序，排序后为“abcedf”，转换后为“5D37BF”

接口设计及说明：
功能:字符串处理
输入:两个字符串,需要异常处理
输出:合并处理后的字符串，具体要求参考文档
返回:无
"""




while True:
    try:
        dic = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        s = input().replace(" ","")
        ss = ""
        odd,even = "",""
        for i,v in enumerate(s):
            if i % 2 == 0:
                even += v
            else:
                odd += v
        odd = "".join(sorted(odd))
        even = "".join(sorted(even))

        for i in range(len(even)):
            if even[i] in "0123456789abcdefABCDEF":
                #print(int(bin(dic.index(even[i].upper())).replace("0b","").rjust(4,"0")[::-1],2))
                ss += dic[int(bin(dic.index(even[i].upper())).replace("0b","").rjust(4,"0")[::-1],2)]
            else:
                ss += even[i]
            if len(odd) != i:
                if odd[i] in "0123456789abcdefABCDEF":
                    ss += dic[int(bin(dic.index(odd[i].upper())).replace("0b","").rjust(4,"0")[::-1],2)]
                else:
                    ss += odd[i]
        print(ss)

    except:
        break


