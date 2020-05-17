#!/usr/bin/python
# _*_ coding:utf-8 _*_
"""
简单的ICMP ping程序
by_0verflow qq1635590569 2020_05_17
如有bug或者改进的地方，望不吝赐教
"""
import time
import os
import sys
from scapy.all import *

def echo_requset(dst,ttl):
    s_id = os.getpid()
    send_time = time.time()  # 记录发包时间 1588772735.7997622
    echo_reply = sr1(IP(dst=dst,ttl=ttl)/ICMP(id=s_id)/b'qwertyuiopasdfghjklzxcvbnm123456',timeout=1,verbose=0)
    try:
        if echo_reply.getlayer(ICMP).type == 0 and echo_reply.getlayer(ICMP).code == 0 and echo_reply.getlayer(ICMP).id == s_id:
            reply_sourec_ip = echo_reply[0].src
            reply_ttl = echo_reply[0].ttl
            rec_time = time.time()
            times = int((rec_time - send_time)*1000)
            reply_len = len(echo_reply[2].load)
            return reply_sourec_ip,times,reply_ttl,reply_len
    except:
        print("不通")

def pinger(dst):
    for i in range(1,5):   # ping5次
        ping_result = echo_requset(dst,i)
        if ping_result:
            print("来自:{} 的回复: 字节={} 延迟={}ms TTL={}".format(ping_result[0],ping_result[3],ping_result[1],ping_result[2]))
        time.sleep(1)
if __name__ == '__main__':
    try:
        dest = sys.argv[1]  # 要ping的ip
        pinger(dest)
    except:
        print("""
        [使用示例]
        python ICMP_request.py [IP地址]    
        """)


