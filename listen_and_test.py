import time
import pytest
import pdfkit

if __name__ == '__main__':
    while 1:
        time.sleep(2)
        print("Test ...")
        pytest.main(['--html=report.html', './http/'])
        pdfkit.from_file('report.html', 'report.pdf')
