# !/usr/bin/python3
# -*-coding:utf-8-*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def send_mail():

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    from_addr = 'service@incopat.cn'
    password = 'Incopat.!@#456'
    to_addr = 'wenbao.qi@incoshare.com'
    smtp_server = 'smtp.incopat.cn'

    msg = MIMEText('邮件内容：hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr('service <%s>' % from_addr)
    msg['To'] = _format_addr('齐文豹 <%s>' % to_addr)
    msg['Subject'] = Header('邮件主题', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
send_mail()