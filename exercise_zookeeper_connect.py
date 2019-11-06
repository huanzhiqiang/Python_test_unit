#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: zookeeper-exercise.py  
@time: 2019/10/11 13:30
"""
import threading
from kazoo.client import KazooClient
from kazoo.protocol.states import KazooState
from kazoo.recipe.watchers import ChildrenWatch
import time,logging

def restart_zk_client():

    '''重启zookeeper会话'''
    global zk_client
    global zk_conn_stat
    try:
        zk_client.restart()
    except Exception as e:
        print('重启zookeeper客户端异常：%s' % e)

def zk_conn_listener(state):
    '''zookeeper连接状态监听器'''
    global zk_conn_stat
    if state == KazooState.LOST:
        print('zookeeper connection lost')
        zk_conn_stat = 1
        # Register somewhere that the session was lost
        thread = threading.Thread(target=restart_zk_client)
        thread.start()

    elif state == KazooState.SUSPENDED:
        print('zookeeper connection dicconnected')
        zk_conn_stat = 2
        # Handle being disconnected from Zookeeper
    else:
        zk_conn_stat = 3
        print('zookeeper connection cconnected/reconnected')
        # Handle being connected/reconnected to Zookeeper

def event_listener(event):
    print(event)

if __name__ == '__main__':
    zk_client=KazooClient(hosts='172.20.32.253:2181')
    zk_client.add_listener(zk_conn_listener)
    zk_client.start()
    print('>>>>>>>',zk_conn_stat)