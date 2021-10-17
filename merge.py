from PyPDF2 import PdfFileReader as Reader 
from PyPDF2 import PdfFileWriter as Writer
from sys import argv
from os import path, mkdir, remove

assert path.exists("./output/meta.txt"), "meta.txt not found, make sure to use split.py first"

meta = open("./output/meta.txt", "r")
lines = meta.readlines()
meta.close()

filename = lines[0].replace("\n", "")
desiredPage = int(lines[1].replace("\n", ""))
numPages = int(lines[2])

assert not path.exists("./output/{0}".format(filename)), "file already exists in output"

print(lines)

assert path.exists("./output/{0}.pdf".format(desiredPage)), "pdf of desired page not found, please make sure to export as pdf once you've made changes"

pdfMerged = Writer()

pdfBeforePath = "./output/1-{0}.pdf".format(desiredPage-1)
if path.exists(pdfBeforePath):
	pdfBefore = Reader(pdfBeforePath)
	pdfMerged.appendPagesFromReader(pdfBefore)
	remove(pdfBeforePath)

pdfDesired = Reader("./output/{0}.pdf".format(desiredPage))
pdfMerged.appendPagesFromReader(pdfDesired)

pdfAfterPath = "./output/{0}-{1}.pdf".format(desiredPage+1, numPages)
if path.exists(pdfAfterPath):
	pdfAfter = Reader(pdfAfterPath)
	pdfMerged.appendPagesFromReader(pdfAfter)
	remove(pdfAfterPath)

pdfMergedWriter = open("./output/{0}".format(filename), "wb")
pdfMerged.write(pdfMergedWriter)
pdfMergedWriter.close()

remove("./output/{0}.pdf".format(desiredPage))
remove("./output/{0}.docx".format(desiredPage))
remove("./output/meta.txt")