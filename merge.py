from PyPDF2 import PdfFileReader as Reader 
from PyPDF2 import PdfFileWriter as Writer
from sys import argv
from os import path, mkdir, remove
from docx2pdf import convert

assert path.exists("./output/meta.txt"), "meta.txt not found, make sure to use split.py first"

meta = open("./output/meta.txt", "r")
lines = meta.readlines()
meta.close()

filename = lines[0].replace("\n", "")
desiredPage = int(lines[1].replace("\n", ""))
numPages = int(lines[2])

print(lines)

assert path.exists("./output/{0}.docx".format(desiredPage)), "docx file not found"

convert("./output/{0}.docx".format(desiredPage), "./output/{0}.pdf".format(desiredPage))

pdfBefore = Reader("./output/1-{0}.pdf".format(desiredPage-1))
pdfDesired = Reader("./output/{0}.pdf".format(desiredPage))
pdfAfter = Reader("./output/{0}-{1}.pdf".format(desiredPage+1, numPages))

pdfMerged = Writer()

pdfMerged.appendPagesFromReader(pdfBefore)
pdfMerged.appendPagesFromReader(pdfDesired)
pdfMerged.appendPagesFromReader(pdfAfter)

pdfMergedWriter = open("./output/{0}".format(filename), "wb")
pdfMerged.write(pdfMergedWriter)
pdfMergedWriter.close()

remove("./output/1-{0}.pdf".format(desiredPage-1))
remove("./output/{0}.pdf".format(desiredPage))
remove("./output/{0}-{1}.pdf".format(desiredPage+1, numPages))
remove("./output/{0}.docx".format(desiredPage))
remove("./output/meta.txt")