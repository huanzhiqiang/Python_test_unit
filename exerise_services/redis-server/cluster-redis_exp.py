#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: cluster-redis_exp.py
@time: 2019/12/18 17:29
"""
from rediscluster import RedisCluster
import time
"""
redis 集群信息：
Using 3 masters:
172.20.32.251:7000
172.20.32.251:7001
172.20.32.252:7000
172.20.32.252:7001
172.20.32.253:7000
172.20.32.253:7001
Adding replica 172.20.32.251:7000 to 172.20.32.251:7001
Adding replica 172.20.32.252:7000 to 172.20.32.252:7001
Adding replica 172.20.32.253:7000 to 172.20.32.253:7001
"""
# 构建所有的节点，Redis会使⽤CRC16算法，将键和值写到某个节点上
startup_nodes = [
    {'host': '172.20.32.251', 'port': '7000'},
    {'host': '172.20.32.252', 'port': '7000'},
    {'host': '172.20.32.253', 'port': '7000'},
]
# startup_nodes = [{"host": "172.20.32.251", "port": "7000"}]
# 构建StrictRedisCluster对象
src = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, password='123com')
# 设置键为key1、值为test-hello-world的数据
result = src.set('key1', 'test-hello-world')
print(result)

while True:
    try:
        # 获取键为name
        name = src.get('key1')
        print(name)
        time.sleep(2)
    except Exception as e:
        print(e)