#!/usr/bin/python
# _*_ coding:utf-8 _*_
"""
调用socket模块进行TCP端口扫描，未完善
"""

from socket import *
import sys

def scanner(dst_ip, d_port):
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        conn.connect((dst_ip, d_port))
        print("[+]{}:{}  =======>  Status: OPEN".format(dst_ip, d_port))
        conn.close()
    except:
        print("[+]{}:{}  =======>  Status: CLOSE".format(dst_ip, dst_ip))

if __name__ == "__main__":
    dst_ip = sys.argv[1]
    dst_port = int(sys.argv[2])
    scanner(dst_ip, dst_port)
