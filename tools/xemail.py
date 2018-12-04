import os
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_to, subject, text, files=None):
    assert isinstance(send_to, list)
    server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
    send_from = os.environ.get('MAIL_ADDR')
    password = os.environ.get('MAIL_PASSWD')
    server.login(send_from, password)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    #smtp = smtplib.SMTP(server)
    server.sendmail(send_from, send_to, msg.as_string())
    server.close()

if __name__ == '__main__':
    outputFilename = 'report.pdf'
    to_addr = [ "804048353@qq.com", "2596416750@qq.com", "1063489610@qq.com"]
    send_mail(to_addr, 'sss','xxxx', [outputFilename, ])
