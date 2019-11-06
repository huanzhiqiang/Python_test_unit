#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: apscheduler-exp1.py  
@time: 2019/10/31 11:19
"""
import time,datetime
curr_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
next_run_time=datetime.datetime.now()+datetime.timedelta(seconds=12)
print(datetime.datetime.now())
print(datetime.timedelta(seconds=12))
print(curr_time)
print(next_run_time)