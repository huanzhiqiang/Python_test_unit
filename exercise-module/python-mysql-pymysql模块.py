#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: system-pymysql.py
@time: 2019/10/16 14:28
"""
import pymysql

config={
    "host":"172.20.32.252",
    "port":3306,
    "user":"root",
    "password":"anbang@123",
    "database":"dbforpymysql"
}

# exp-01 基本方式
db=pymysql.connect(**config)
cursor = db.cursor()
sql = "INSERT INTO userinfo(username,passwd) VALUES('hzq','123@123')"
cursor.execute(sql)
db.commit()  #提交数据
cursor.close()
db.close()

# exp-02 传参方式
db=pymysql.connect(**config)
cursor=db.cursor()
sql='insert into userinfo(username,passwd) value (%s,%s)'
cursor.execute(sql,("hehe","123.com"))
db.commit()
cursor.close()
db.close()

#exp-03 方式三
def My_Pymysql(user,pwd):
    db = pymysql.connect(**config)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    print("@@@@@@@@@@@@@%s,%s"%(user,pwd))
    sql = "select * from userinfo where username='%s' and passwd='%s'"%(user,pwd)
    print(">>>>>>>>>>>>>>>>>>>>>>",sql)
    result=cursor.execute(sql)
    cursor.close()
    db.close()
    if result:
        print('登录成功')
    else:
        print('登录失败')

user=input(">>>>>>>>>")
passd=input(">>>>>>>>")
My_Pymysql(user,passd)


# 方式四 批量插入数据；
db=pymysql.connect(**config)
cursor=db.cursor()
sql='insert into userinfo(username,passwd) value (%s,%s)'
cursor.executemany(sql,[("tom","1234"),("exilt","321")])
db.commit()
cursor.close()
db.close()

# 方式五： 删除数据返回结果为1
db=pymysql.connect(**config)
cursor=db.cursor()
sql="delete from userinfo where username=%s"
res=cursor.executemany(sql,("hzq",))
print("res=",res)
db.commit()
cursor.close()
db.close()

#方式六查询自增ID
db=pymysql.connect(**config)
cursor=db.cursor()
sql="insert into userinfo(username,passwd)value (%s,%s)"
cursor.execute(sql,("dddd","12323432"))
print("the last rowid is",cursor.lastrowid)
db.commit()
cursor.close()
db.close()

#方式七；查询数据；
db=pymysql.connect(**config)
cursor=db.cursor()
sql="select * from userinfo"
cursor.execute(sql)
#####fetchone():获取下一行数据，第一次为首行； 结果元组
res=cursor.fetchone()
print(res)
res=cursor.fetchone()
print(res)

#####fetchall():获取所有行数据源 结果是元组类型；
res=cursor.fetchall()
print(res)
cursor.close()
db.close()

# 方式八： 结果列表---字典类型 [{'id': 1, 'username': 'frank', 'passwd': '123'}, {'id': 2, 'username': 'rose', 'passwd': '321'}]
db=pymysql.connect(**config)
cursor=db.cursor(cursor=pymysql.cursors.DictCursor)
sql="select * from userinfo"
cursor.execute(sql)
res=cursor.fetchall()
print(res)
cursor.close()
db.close()

# 方式九 上下文管理；
db=pymysql.connect(**config)
with db.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
    sql="select * from userinfo"
    cursor.execute(sql)
    res=cursor.fetchone()
    print(res)
    cursor.scroll(2,mode='relative')
    res=cursor.fetchone()
    print(res)
    cursor.close()
db.close()

def cursor_it():
    db = pymysql.connect(**config)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    return cursor

def select_sql():
    cur=cursor_it()
    sql = "select * from userinfo"
    cur.execute(sql)
    res=cur.fetchone()
    cur.close()

    return res

print(select_sql())