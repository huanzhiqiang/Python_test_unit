#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: prometheus_way.py  
@time: 2019/10/30 11:09
"""
import prometheus_client
from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry
import requests

def v1():  # 获取监控数据的值
    return 11.5

def v2():
    return 1.80

n1 = v1()
n2 = v2()

REGISTRY = CollectorRegistry(auto_describe=False)
# 自定义指标必须利用CollectorRegistry进行注册，注册后返回给prometheus
# CollectorRegistry必须提供register，一个指标收集器可以注册多个collectoryregistry


jin = Gauge("kou", "zhegezuoyongshijinkoudaxiao", ["l1", 'l2', 'instance'], registry=REGISTRY)
chu = Gauge("chu_kou", "zhegezuoyongshichukoudaxiao", ["l1", 'l2', 'instance'], registry=REGISTRY)
# “jin_kou” 指标名称
# "zhegezuoyongshichukoudaxiao"  指标的注释信息
# "[]"  定义标签的类别及个数

jin.labels(l1="label1", l2="label2", instance="windows1").inc(n1)
chu.labels(l1="label1", l2="label2", instance="windows1").inc(n2)
# “[]”中有几个，就需要写几个个数要完全一致

requests.post("http://120.78.149.223:9092/metrics/job/python/", data=prometheus_client.generate_latest(REGISTRY))
# 向指定的API发送post信息，将注册的信息发过去
# API中的 “python”是 job的名字