"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
import os

server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
from_addr = os.environ.get('MAIL_ADDR')
password = os.environ.get('MAIL_PASSWD')
print(from_addr, password)

to_addr = [ "804048353@qq.com", "2596416750@qq.com"]
#Next, log in to the server
server.login(from_addr, password)
server.set_debuglevel(1)
#server.starttls()  
#Send the mail

msg = """
Hello!""" # The /n separates the message from the headers
server.sendmail(from_addr, to_addr, msg)
