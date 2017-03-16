#!/usr/bin/env python3
# --*-- coding:utf8 --*--

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

#from_addr = input('From:')
#password = input('Password:')
#to_addr = input('To:')
#smtp_server = input('SMTP Server:')
from_addr = 'lucj@visionet.com.cn'
password = 'Lcj921010'
to_addr = 'luchuanjia@msn.com'
smtp_server = 'smtp.263.net'
smtp_port = '587'


msg = MIMEText('Hello, send by Python...','plain','utf-8')
msg['From'] = _format_addr('Python 爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...','utf-8').encode()

server = smtplib.SMTP(smtp_server,smtp_port)

server.starttls()

server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
