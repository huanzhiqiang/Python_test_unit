#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: huanzhiqiang  
@file: tomcat_log_exp.py  
@time: 2019/12/24 11:26
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import getsize
from sys import exit
from re import compile,IGNORECASE
#定义主机 帐号 密码 收件人 邮件主题
mail_info = {
 "from": "961502365@qq.com",
 "to": "67785783@qq.com",
 "hostname": "smtp.qq.com",
 "username": "961502365@qq.com",
 "password": "lvwaplbliknlbehj",
 "mail_subject": "Server Error",
 "mail_text": "hello!\n tomcat服务器出现异常了!,请及时处理:\n",
 "mail_encoding": "utf-8"
}
#定义tomcat日志文件位置
tomcat_log = 'E:\\develop-dyin\\modules-exp\\app_logs\\log.txt'
#该文件是用于记录上次读取日志文件的位置,执行脚本的用户要有创建该文件的权限
last_position_logfile = 'E:\\develop-dyin\\modules-exp\\app_logs\\postion_exp.txt'
#匹配的错误信息关键字的正则表达式
pattern = compile(r'Error|^\t+\bat\b',IGNORECASE)
#发送邮件函数
def send_mail(error):
    msg=MIMEMultipart('mixed')
    msg['Subject']=mail_info['mail_subject']
    msg['From']=mail_info['from']
    msg['To']=mail_info['to']
    text=mail_info['mail_text'] + error
    ##文件本构造
    text_plain=MIMEText(text,'plain','utf-8')
    msg.attach(text_plain)

    ##发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(mail_info['hostname'])
    # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    # smtp.set_debuglevel(1)
    smtp.login(mail_info['username'], mail_info['password'])
    smtp.sendmail(mail_info['from'], mail_info['to'], msg.as_string())
    smtp.quit()

#读取上一次日志文件的读取位置
def get_last_position(file):
 try:
    data = open(file,'r')
    last_position = data.readline()
    if last_position:
        last_position = int(last_position)
    else:
        last_position = 0
 except:
    last_position = 0
 return last_position

# #写入本次日志文件的本次位置
def write_this_position(file,last_positon):
    try:
        data = open(file,'w')
        data.write(str(last_positon))
        data.write('\n' + "Don't Delete This File,It is Very important for Looking Tomcat Error Log !! \n")
        data.close()
    except:
        print ("Can't Create File !" + file)
        exit()

#分析文件找出异常的行
def analysis_log(file):
    error_list = []
    try:
        data = open(file,'r')
        last_position = get_last_position(last_position_logfile)
        this_postion = getsize(tomcat_log)
        if this_postion < last_position:
            data.seek(0)
        elif this_postion == last_position:
            exit()
        elif this_postion > last_position:
            data.seek(last_position)
        for line in data:
            if pattern.search(line):
                error_list.append(line)
        write_this_position(last_position_logfile,data.tell()) #写入本次读取的位置
        data.close()
    except:
        exit()
    return ''.join(error_list)        #形成一个字符串

def main():
    #调用发送邮件函数发送邮件
    error_info = analysis_log(tomcat_log)
    print(error_info)
    if error_info:
        send_mail(error_info)

if __name__ == '__main__':
    main()
