#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: active-exp2.py  
@time: 2019/11/27 13:41
"""

from multiprocessing import Pool
import os, time


def long_timw_task(name, start, secod):
    print('Run task %s (%s).....' % (name, os.getpid()))
    print('parent process is {}'.format(os.getppid()))
    x = 0
    while time.time() - start < secod:
        x = x ^ 1


if __name__ == '__main__':
    start = time.time()
    long_timw_task('sub_main', start, 10)
    p = Pool(2)
    for i in range(5):
        p.apply_async(long_timw_task, args=(i, start, 80,))
    print('Waiting for all subprocessess done....')
    p.close()
    p.join()
    print('All subprocesss.....')

