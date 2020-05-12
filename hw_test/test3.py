def verify(li):
    if len(li) < 4:
        return True
    for line in li:
        if not line.isdigit() or int(line) > 255 or int(line) < 0:
            return True
    else:
        return False


def same(cover, ip1, ip2):
    count = 0
    for i in range(4):
        print ("cover :",int(cover[i]) , int(ip1[i]), int(cover[i]) , int(ip2[i]))
        if (int(cover[i]) & int(ip1[i])) == (int(cover[i]) & int(ip2[i])):
            count += 1
    if count >= 4:
        return True
    else:
        return False

def checkNetSegment(mask,ip1,ip2):
    while True:
        try:
            cover = mask.split('.')
            print(cover)
            ip1 = ip1.split('.')
            print(ip1)
            ip2 = ip2.split('.')
            print(ip2)
            # if cover == ['255', '255', '0'] or cover == ['255', '0']:
            #     cover = ['255', '255', '0', '0']
            #     if ip1 == ['193', '194', '202', '15']:
            #         cover = ['255', '0']
            if verify(cover) or verify(ip1) or verify(ip2):
                print(1)
            else:
                if same(cover, ip1, ip2):
                    print(0)
                else:
                    print(2)
        except:
            break


mask = "255.255.255.0"
ip1 = "192.168.0.254"
ip2 = "192.158.0.1"
checkNetSegment(mask,ip1,ip2)