#!/usr/bin/python
#encoding=utf8
import smtplib
import string

#mem=psutil.virtual_memory()
class mail:
    def __init__(self,TO,text):
        self.TO=TO
        self.text=text

    def send_mail(self):
        HOST="smtp.qq.com"
        SUBJECT="Test email for python by gx"
        TO=self.TO
        FROM="10779164@qq.com"
        #text="ÄãºÃ°¡£¬Ð¡ÅóÓÑ£¡"
        BODY=string.join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject %s" % SUBJECT,
            "",
            self.text
            ),"\r\n")
        try:
            server=smtplib.SMTP_SSL()
            server.connect(HOST,"465")
            #server.starttls()
            server.login("10779164@qq.com","sriudeacxlmocaec")  ##Õâ¸öÃÜÂëÊÇ¿ªÆôÓÊÏäSMTP·þÎñÊ±´úÌæQQÃÜÂëµÄÑéÖ¤Âë
            server.sendmail(FROM,TO,BODY)
            server.quit()
            return "Successful"
        except Exception,e:
            return "fail"+str(e)

