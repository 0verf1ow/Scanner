#!/usr/bin/python
# _*_ coding=utf=8 _*_
"""
简单的TCP端口扫描程序
by_0verflow qq1635590569 2020_05_17
如有bug或者改进的地方，望不吝赐教
"""

from scapy.all import *
import sys
import time

def port_scan(dst_ip,port,*args):
    if len(args) == 1:
        result_raw = sr(IP(dst=dst_ip)/TCP(dport=(port,args[0])),timeout=2,verbose=0)
        print_res(result_raw[0])
    else:
        result_raw = sr(IP(dst=dst_ip)/TCP(dport=port),timeout=2, verbose=0)
        print_res(result_raw[0])

def print_res(res):
    print("[+]扫描 {} 的结果如下:\n".format(res[0][1][0].src))
    for i in res:
        if i[1][1].flags == "SA":
            print("[+] PORT:{}  ======>  Status: OPEN".format(i[1][1].sport))
    end_time = time.time()
    scan_time = (end_time - start_time)
    print("\n扫描结束,所用时间 {:.2f}s".format(scan_time))
if __name__ == "__main__":
    start_time = time.time()
    if len(sys.argv) == 3:
        dst_ip = sys.argv[1]
        port = int(sys.argv[2])
        port_scan(dst_ip,port)
    elif len(sys.argv) == 4:
        dst_ip = sys.argv[1]
        port = int(sys.argv[2])
        max_port = int(sys.argv[3])
        port_scan(dst_ip,port,max_port)
    else:
        print("""
        【用法示例】
        扫描单个端口：python scapy_port_scan.py [目标IP] [指定端口]
        扫描指定范围端口：python scapy_port_scan.py [目标IP] [开始端口] [结束端口]
        """)
