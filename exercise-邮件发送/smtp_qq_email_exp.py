#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author: hXXXXzhXqXX
@file: yagmail-exp1.py
@time: 2019/10/15 14:13
"""

import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

smtpserver = 'smtp.qq.com'
username = 'XXXXX@qq.com'
password='fvfXXXXXeetbdci'
sender='96XXXX@qq.com'
receiver=['96XXXX@qq.com','XXXX83@qq.com']

subject = 'python UB测试邮件'
subject=Header(subject, 'utf-8').encode()
msg=MIMEMultipart('mixed')
msg['Subject']=subject
msg['From']='XXXXXX365@qq.com'
msg['To']=";".join(receiver)


#构造文字内容
text = "Hi!\nXXXX接口不可用了！\n请查看相关接口是否在线:\nhttp://192.168.0.3:9081/Ninvoicejs/serve/invoice?wsdl"
text_plain = MIMEText(text,'plain', 'utf-8')
msg.attach(text_plain)

html = """
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       Warning content:<br>
       Interface information: <a href="http://www.baidu.com">link</a> No more.<br>
    </p>
  </body>
</html>
"""
text_html = MIMEText(html,'html', 'utf-8')
text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
msg.attach(text_html)


#发送邮件
# smtp = smtplib.SMTP()
# smtp.connect('smtp.163.com')
# smtp.login(username, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()

smtpobj=smtplib.SMTP_SSL(smtpserver,465)
smtpobj.login(username,password)
smtpobj.sendmail(sender,receiver,msg.as_string())
print("邮件发送成功")
smtpobj.quit()#退出