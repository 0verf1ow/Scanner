# coding:utf-8
"""

一个简单的ARP发现程序
需要安装scapy模块
by_0verflow 2020.5.4

"""
# import sys
from scapy.all import *

def arp_scan():
    # my_ip = sys.argv[1]
    # mask = sys.argv[2]
    my_ip = get_if_addr(conf.iface)     # scapy内置方法获取本机ip
    # my_mac = get_if_hwaddr(conf.iface)  # scapy内置方法获取本机mac
    """发包"""
    ans, unans = srp((Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = my_ip+"/24")),verbose = 0, timeout = 2)
    """循环取出收到的ARP响应"""
    for i in ans:
        ip = i[1][1].psrc
        mac = i[1][1].hwsrc
        print("[+] IP地址:{}  ==>  MAC地址:{}".format(ip,mac))


if __name__ == "__main__":
    arp_scan()