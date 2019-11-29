#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: acticemq-exp.py  
@time: 2019/11/27 11:08
"""
import stomp
import time
import random

queue_name = '/queue/SampleQueue'
topic_name = '/topic/SampleTopic'
listener_name = 'SampleListener'
post = 61613


class SampleListener(object):
    def on_message(self, headers, message):
        print('headers: %s' % headers)
        print('message: %s' % message)


# 推送到队列queue
def send_to_queue(msg):
    conn = stomp.Connection10([('192.168.56.12', post)])
    conn.start()
    conn.connect()
    conn.send(queue_name, msg)
    conn.disconnect()


# 推送到主题
def send_to_topic(msg):
    conn = stomp.Connection10([('192.168.56.12', post)])
    conn.start()
    conn.connect()
    conn.send(topic_name, msg)
    conn.disconnect()


##从队列接收消息
def receive_from_queue():
    conn = stomp.Connection10([('192.168.56.13', 61615)])
    print(">>>>>>>>>>>>>>>>>>>>>11")
    conn.set_listener(listener_name,SampleListener())
    conn.start()
    conn.connect()
    conn.subscribe(queue_name)
    time.sleep(1)  # secs
    conn.disconnect()

##从队列接收消息
def receive_f_queue():
    conn = stomp.Connection10([('192.168.56.12', 61613)])
    print(">>>>>>>>>>>>>>>>>>>>>>>>12")
    conn.set_listener(listener_name,SampleListener())
    conn.start()
    conn.connect()
    conn.subscribe(queue_name)
    time.sleep(1)  # secs
    conn.disconnect()

##从主题接收消息
def receive_from_topic():
    conn = stomp.Connection10([('192.168.56.13', 61615)])
    conn.set_listener(listener_name, SampleListener())
    conn.start()
    conn.connect()
    conn.subscribe(topic_name)
    while 1:
        send_to_topic('topic')
        time.sleep(3)  # secs
    conn.disconnect()


if __name__ == '__main__':
    while 1:
        send_to_queue('{23234:1233}')
        time.sleep(1)
        # func=random.choice([receive_from_queue,receive_f_queue])
        # func()
    # receive_f_queue()
    # send_to_topic('hzq-tipc')
    # receive_from_topic()