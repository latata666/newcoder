# -*- coding: utf-8 -*-

"""
/*
* 功能: 判断两台计算机IP地址是同一子网络。
* 输入参数：    String Mask: 子网掩码，格式：“255.255.255.0”；
*               String ip1: 计算机1的IP地址，格式：“192.168.0.254”；
*               String ip2: 计算机2的IP地址，格式：“192.168.0.1”；
*

* 返回值：      0：IP1与IP2属于同一子网络；     1：IP地址或子网掩码格式非法；    2：IP1与IP2不属于同一子网络
*/
public int checkNetSegment(String mask, String ip1, String ip2)
{
    /*在这里实现功能*/
    return 0;
}
"""

def ipTobin(ip):
    ip_list = ip.split(".")
    for i in range(len(ip_list)):
        ele = bin(int(ip_list[i]))
        ip_list[i] = ele[2:]
        if len(ip_list[i] )< 8:
            strl = "0" * (8 -len(ip_list[i]) ) + ip_list[i]
            ip_list[i] = strl

    #print("ele_num",ip_list)
    return ip_list


def cmpip(mask,ip):
    list=[]
    for i in range(len(ip)):
        #print(i,int(mask[i]) ,int(ip[i]))
        result = int(mask[i]) & int(ip[i])
        list.append(result)
    #print(list)

    return list

def check(str):
    if len(str) < 4:
        return 1
    for line in str:
        if not line.isdigit() or int(line) > 255 or int(line) < 0:
            return 1
        else:
            return 0

def checkNetSegment(mask,ip1,ip2):
    #print(mask, ip1, ip2)
    if(check(mask) or check(ip1) or check(ip2)):
        return 1

    ele_mask = ipTobin(mask)
    ele_ip1 = ipTobin(ip1)
    ele_ip2 = ipTobin(ip2)
    if ( cmpip(ele_mask,ele_ip1) == cmpip(ele_mask,ele_ip2)):
        return 0
    else:
        return 2





mask = "255.0.0.0"
ip1 = "192.167.0.254"
ip2 = "232.43.7.59"
print(checkNetSegment(mask,ip1,ip2))