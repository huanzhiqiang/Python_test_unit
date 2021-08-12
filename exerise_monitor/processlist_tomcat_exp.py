#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: tomcat-monitor-exp.py  
@time: 2019/12/20 15:48
"""
import os,sys,re
def isRunning(process_name):
    try:
        process = os.popen('ps -ef|grep -v grep|grep -w "' +process_name+ '"').readlines()
        P_M=[]
        for index,name in enumerate(process):
            pattern = re.compile('python')
            match = pattern.findall(name)
            if not match:
                P_M.append(name)
        if len(P_M) >= 1:
            print(1)
            return True
        else:
            print(0)
            return False
    except:
        print("Check process ERROR!!!")
        return False
if __name__ == '__main__':
    p_name=sys.argv[1]
    isRunning(p_name)

