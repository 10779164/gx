#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText
import sys

mail_host = 'smtp.exmail.qq.com'
mail_user = 'caimeiyi@zongshangkeji.com'
mail_postfix = 'qq.com'
mail_password = 'Cmy!123'

def send_mail(to_list,subject,content):
    me = "zabbix admin"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list

    try:
        s = smtplib.SMTP_SSL()
        s.connect(mail_host,465)
	#s.starttls()
        s.login(mail_user,mail_password)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

if __name__ == "__main__":
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])




