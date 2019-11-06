#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: nginx_mon_exp.py  
@time: 2019/10/31 14:49
"""
import psutil
import os,sys

#获取主机名称；
def hostname():
    sys=os.name
    if sys == 'nt':
        hostname=os.getenv('computername')
        return hostname
    elif sys == 'posix':
        hosts=os.popen('echo $HOMENAME')
        try:
            hostname=hosts.read()
            return hostname
        finally:
            hosts.close()
    else:
        return 'Unkwon hostname'

#获取进程状态
# def processStatus(processName):
#     pids=psutil.pids()
#     a=1
#     for pid in pids:
#         p=psutil.Process(pid)
#         if p.name()==processName:
#             print(a) #进程存活为1
#             a+=1
#     if a==1:
#         print(0) #进程不存活为0

#获取进程ID
def proceessPID(processName):
    pids=psutil.pids()
    for pid in pids:
        p=psutil.Process(pid)
        if p.name()==processName:
            return (True,pid)
    else:
        print('找不到进程'+processName)
        return False

#获取进程的端口号
def processPort(pid):
    p=psutil.Process(pid)
    data=p.connections()
    data_listen=[x for x in data if 'LISTEN' in x]
    if len(data_listen) == 1:
        return list(data_listen[0][3])[1]
    elif len(data_listen) > 1:
        n_p=[]
        for amt in range(0,len(data_listen)):
            pp=list(data_listen[amt][3])[1]
            n_p.append(pp)
            return n_p
    else:
        return 0
if __name__ == '__main__':
    hostname=hostname().strip()
    # PID=proceessPID('nginx')
    # port=processPort(PID[1])
    # json_data=[{'name': hostname+'-nginx','port':port,'PID':PID}]
    # print(json_data)
    print(hostname)
