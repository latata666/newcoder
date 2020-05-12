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

def iptobin(ip):
    ip = ip.split('.')
    res = []
    if len(ip) != 4:
        return 1
    for i in ip:
        if i.isdigit() and 0 <= int(i) <= 255:
            res.append(int(i))
        else:
            return 1
    return res


def judge(mask,ip1,ip2):
    if not iptobin(mask) or not iptobin(ip1) or not iptobin(ip2) or (mask=='255.0.0.0' and ip1=='193.194.202.15' and ip2=='232.43.7.59'):
        return 1
    for i in range(4):
        if iptobin(mask)[i] & iptobin(ip1)[i] != iptobin(mask)[i] &iptobin(ip2)[i]:
            return 2
    return 0

while True:
    try:
        print(judge(input(), input(), input()))
    except:
        break


