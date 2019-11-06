#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: zookeeper-exercise2.py  
@time: 2019/10/11 16:31
"""
import sys
from kazoo.client import KazooClient

def main():
    try:
        nodedir='/huanzhiqiang'
        host='172.20.32.253'
        port='2181'
        timeout=100
        zkc=KazooClient(hosts=host+':'+port,timeout=timeout)
        zkc.start()

        if zkc.exists(nodedir+'123'):
            print(nodedir+'123','不存在')
        else:
            childrenpath=zkc.create(nodedir+'123','test123')
            print('创建节点：',childrenpath,'成功')
            zkc.create(nodedir+'test999','test9999',ephemeral=True)
        dataAndStat=zkc.get(nodedir)
        data=dataAndStat[0]
        print('数据为:',data)
        stat=dataAndStat[1]
        print("数据版本号：",stat.version)
        print("数据长度：",stat.data_length)

