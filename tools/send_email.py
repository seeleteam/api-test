"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(report_file):
    server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
    from_addr = os.environ.get('MAIL_ADDR')
    password = os.environ.get('MAIL_PASSWD')
    
    to_addr = [ "804048353@qq.com", "2596416750@qq.com", "1063489610@qq.com"]
    #Next, log in to the server
    server.login(from_addr, password)
    server.set_debuglevel(1)
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart()
    msg.attach(MIMEText(file(report_file).read()))
    
    server.sendmail(from_addr, to_addr, 'kkkk')
