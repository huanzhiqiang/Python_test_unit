#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: mem_use_exp.py  
@time: 2019/11/29 10:41
"""
import sys,os
import re
import time

def print_help():
    print ('Usage: ')
    filename=os.path.basename(__file__)
    print ('  python %s 100MB'%filename)
    print ('  python %s 1GB'%filename)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        pattern = re.compile('^(\d*)([M|G]B)$')
        match = pattern.match(sys.argv[1].upper())
        if match:
            num = int(match.group(1))
            unit = match.group(2)
            if unit == 'MB':
                s = ' ' * (num * 1024 * 1024)
            else:
                s = ' ' * (num * 1024 * 1024 * 1024)
            time.sleep(10000)
        else:
            print_help()
    else:
        print_help()
