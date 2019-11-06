#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: kirmate_map_exp1.py  
@time: 2019/10/23 16:04
"""
import json
from urllib.request import urlopen, quote
import requests,csv
# import pandas as pd
#导入这些库后边都要用到
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'uKsQZE7yAGMYAIFCzVU0UHvm'
    # ak = 'ijPQplt71W0cUo6oQGcp9ASYQLPQjnHQ'
    add = quote(address) #由于本文城市变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    return temp

if __name__ == '__main__':
    print(getlnglat("天津市东丽区听湖小镇"))