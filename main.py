import pytest
from tools.html2pdf import convertHtmlToPdf
from tools.xemail import send_mail

# test
pytest.main(['--html=report.html', './http/'])

# covert html to pdf
sourceFilename = 'report.html'
outputFilename = 'report.pdf'
convertHtmlToPdf(sourceFilename, outputFilename)

# send an email
to_addr = [ "804048353@qq.com", "2596416750@qq.com", "1063489610@qq.com"]
subject = "go-seele test"
context = " A file called report.pdf contains a complete report generated automatically with information for errors."
attachFiles = [outputFilename, ]
send_mail(to_addr, subject, context, attachFiles)
