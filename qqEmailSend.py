#!/usr/bin/env python 
#_*_coding:utf-8_*_
from email.mime.text import MIMEText
import smtplib

class UserSendEmail(object):
    msg_from = "954960369@qq.com"
    passwd = 'uyzvamliryxtbeab'
    def __init__(self,to_email):
        self.to_email = to_email
        info = self.emailMsg()
        self.sendEmail(self.to_email,info[0],info[1])

    def emailMsg(self):
        subject = raw_input("请输入邮件主题:")
        contents = raw_input("请输入邮件内容:")
        info = [subject,contents]
        return info

    def sendEmail(self,to_email,subject,contens):
        # 设置邮件必备参数
        msg = MIMEText(contens,'plain','utf-8')
        msg['subject'] = subject
        msg['to'] = to_email
        msg['from'] = self.msg_from
        # 发送邮件
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com",465)
            s.login(self.msg_from,self.passwd)
            s.sendmail(self.msg_from,to_email,msg.as_string())
            print "发送成功!"
        except Exception as f:
            print "发送失败，because:%s"%f
        finally:
            s.quit()
if __name__ == "__main__":
    UserSendEmail('liujunhang2013@163.com')