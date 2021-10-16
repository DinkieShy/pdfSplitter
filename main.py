from PyPDF2 import PdfFileReader as Reader 
from PyPDF2 import PdfFileWriter as Writer
from sys import argv
from os import path, mkdir

assert len(argv) >= 3, "USAGE: main.py [filename] [page number]"
if argv[1][-4:] != ".pdf":
	argv[1] += ".pdf"
assert path.isfile(argv[1]), "filename does not exist"

if not path.exists("./output"):
	mkdir("./output")

reader = Reader(argv[1])

desiredPage = int(argv[2])
assert desiredPage <= reader.getNumPages(), "page number out of bounds"

pages = reader.pages

pdfBefore = Writer()
pdfDesired = Writer()
pdfAfter = Writer()
desiredPageIndex = desiredPage - 1

for i in range(reader.getNumPages()):
	if i < desiredPageIndex:
		pdfBefore.addPage(pages[i])
	elif i > desiredPageIndex:
		pdfAfter.addPage(pages[i])
	else:
		pdfDesired.addPage(pages[i])

outputFileBefore = open("./output/1-{0}.pdf".format(desiredPage-1), "wb")
outputFileDesired = open("./output/{0}.pdf".format(desiredPage), "wb")
outputFileAfter = open("./output/{0}-{1}.pdf".format(desiredPage+1, len(pages)), "wb")

pdfBefore.write(outputFileBefore)
pdfDesired.write(outputFileDesired)
pdfAfter.write(outputFileAfter)

outputFileBefore.close()
outputFileDesired.close()
outputFileAfter.close()