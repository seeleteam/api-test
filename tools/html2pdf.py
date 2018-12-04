from xhtml2pdf import pisa             # import python module



# Utility function
def convertHtmlToPdf(sourceFilename, outputFilename):
    with open(sourceFilename, "r") as fd:
	    sourceHtml = fd.read()
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err

# Main program
if __name__ == "__main__":
    pisa.showLogging()
    sourceFilename = 'report.html'
    outputFilename = 'test.pdf'

    convertHtmlToPdf(sourceFilename , outputFilename)
