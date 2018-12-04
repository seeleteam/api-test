"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
from_addr = os.environ.get('MAIL_ADDR')
password = os.environ.get('MAIL_PASSWD')

to_addr = [ "804048353@qq.com", "2596416750@qq.com"]
#Next, log in to the server
server.login(from_addr, password)
server.set_debuglevel(1)
# Create message container - the correct MIME type is multipart/alternative.
#msg = MIMEMultipart('alternative')
msgRoot = MIMEMultipart('related')
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

with open("report.html", "r") as fd:
    #html = fd.read()
    #part = MIMEText(html, 'html')
    #msg.attach(part)
    alert_msg = MIMEText(fd.read(),"html", "utf-8")
    msgRoot.attach(alert_msg)

server.sendmail(from_addr, to_addr, msgRoot.as_string())
