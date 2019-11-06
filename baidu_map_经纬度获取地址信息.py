#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: kirmate_map_exp2.py  
@time: 2019/10/23 16:13
"""
#encoding=utf8  #编码

import json
import urllib.request

#基于百度地图API下的经纬度信息来解析地理位置信息
def getlocation(lat,lng):
    #31.809928, 102.537467, 3019.300
    #lat = '31.809928'
    #lng = '102.537467'
    url = 'http://api.map.baidu.com/reverse_geocoding/v3/?location=' + lat + ',' + lng + '&output=json&coordtype=wgs84ll&ak=ijPQplt71W0cUo6oQGcp9ASYQLPQjnHQ'
    req = urllib.request.urlopen(url)  # json格式的返回数据
    res = req.read().decode("utf-8")  # 将其他编码的字符串解码成unicode
    return json.loads(res)

#json序列化解析数据(lat:纬度，lng:经度)
def jsonFormat(lat,lng):
    str = getlocation(lat,lng)
    dictjson={}#声明一个字典
    #get()获取json里面的数据
    jsonResult = str.get('result')
    formatted_address=jsonResult.get('formatted_address')
    address = jsonResult.get('addressComponent')

    print(">>>>>",formatted_address)
    #国家
    country = address.get('country')
    #国家编号（0：中国）
    country_code = address.get('country_code')
    #省
    province = address.get('province')
    #城市
    city = address.get('city')
    #城市等级
    city_level = address.get('city_level')
    #县级
    district = address.get('district')
    #街道
    street = address.get('street')
    #把获取到的值，添加到字典里（添加）
    dictjson['country']=country
    dictjson['country_code'] = country_code
    dictjson['province'] = province
    dictjson['city'] = city
    dictjson['city_level'] = city_level
    dictjson['district'] = district
    dictjson['street'] = street
    dictjson['formatted_address']=formatted_address
    return dictjson


if __name__ == '__main__':
    # lat = '39.09233234281453'
    # lng = '117.32056850791443'
    # lng='117.47414200942531'
    # lat='39.175033129770014'
    lng='117.47414200942531'
    lat='39.175033129770014'

    # jsonFormat(getlocation(lat,lng))
    # print(getlocation(lat,lng))
    print(jsonFormat(lat,lng))