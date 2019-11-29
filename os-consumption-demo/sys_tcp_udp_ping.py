#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang
@file: threed_ping.py
@time: 2019/11/12 10:35
"""
import threading, subprocess
from time import time
import queue,sys
import socket
import nmap

queue = queue.Queue()
class ThreadUrl(threading.Thread):
    def __init__(self, queue,port):
        threading.Thread.__init__(self)
        self.queue = queue
        self.port = port
    def run(self):
        while True:
            host = self.queue.get()
            port = self.port
            ret = subprocess.call('ping -c 1 -w 1 ' + host, shell=True, stdout=open('/dev/null', 'w'))
            if ret:
                # 主机不存活
                ip_con_down_tx="%s is down \n" % host
                with open('ip_down.txt','a') as d_f:
                    d_f.write(ip_con_down_tx)
            else:
                Client_tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                Client_tcp_sock.settimeout(1)
                try:
                    tcp_result = Client_tcp_sock.connect_ex((host, port))
                    if tcp_result == 0:
                        # tcp端口存在
                        con_tcp_up_txt = "%s:%s is TCP Port exist \n" % (host, port)
                        with open('ip_tcp_open.txt', 'a') as a_f:
                            a_f.write(con_tcp_up_txt)
                    else:
                        nm = nmap.PortScanner()
                        nm.scan(hosts=host, arguments='-p '+str(port) + ' -sU ')
                        hosts_list = [(x, nm[x][u'udp'][port]['state']) for x in nm.all_hosts()]
                        for host, status in hosts_list:
                            print('{0}:{1}'.format(host, status))
                            if status != 'closed':
                                # udp端口存在
                                con_udp_up_txt = "%s:%s is UDP Port exist \n" % (host, port)
                                with open('ip_udp_open.txt', 'a') as a_f:
                                    a_f.write(con_udp_up_txt)
                            else:
                                # 主机存活,但端口不存在;
                                ip_con_up_txt = "%s is up\n" % host
                                with open('ip_up.txt', 'a') as ip_f:
                                    ip_f.write(ip_con_up_txt)
                except Exception :
                    Client_tcp_sock.close()
                    print("Tcp socket错误！")
                Client_tcp_sock.close()
            self.queue.task_done()
def main():
    for i in range(100):
        t = ThreadUrl(queue,port)
        t.setDaemon(True)
        t.start()
    for n in range(len(a)):
        queue.put(a[n])
    queue.join()

if __name__ == '__main__':
    a = []
    with open('ip.txt') as f:
        for line in f.readlines():
            a.append(line.split()[0])
        print(a)

    start = time()
    port=8800
    main()
    print("Elasped Time:%s" % (time() - start))
    sys.exit(0)
