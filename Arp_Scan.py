# coding:utf-8
"""
简单的ARP发现程序
by_0verflow qq1635590569 2020_05_17
如有bug或者改进的地方，望不吝赐教
"""
# import sys
from scapy.all import *
import time

def arp_scan():
    # my_ip = sys.argv[1]
    # mask = sys.argv[2]
    my_ip = get_if_addr(conf.iface)     # scapy内置方法获取本机ip
    # my_mac = get_if_hwaddr(conf.iface)  # scapy内置方法获取本机mac
    """发包"""
    ans, unans = srp((Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = my_ip+"/24")),verbose = 0, timeout = 2)

    print("[+]扫描结果如下\n")
    """循环取出收到的ARP响应"""
    for i in ans:
        ip = i[1][1].psrc
        mac = i[1][1].hwsrc
        print("[+] IP地址:{}  ==>  MAC地址:{}".format(ip,mac))
    end_time = time.time()
    scan_time = end_time - start_time  # 计算扫描时间
    print("\n扫描结束,所用时间 {:.2f}s".format(scan_time))
if __name__ == "__main__":
    start_time = time.time()
    arp_scan()