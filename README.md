# pdfSplitter
I hate having to mess with many-paged PDFs, so here's some code to spit out a docx of the page I want to edit, and then merge it back as if I was paying Adobe

## Setup
Step 1: Download as zip and extract, or clone  
Step 2: Navigate in a terminal to the folder you just downloaded  
Step 3: Run `pip install -r requirements.txt` (You may wish to do this in a [virtual environment](https://docs.python.org/3/library/venv.html), but don't forget to enable it!)

## Use
Step 1: Run `python split.py` for a usage example  
Step 2: Make changes to the docx created in the output folder then save/export as a pdf  
Step 3: Run `python merge.py`  

Split.py: Creates 2 pdfs and a docx: pages before (pdf), the page you want to edit (docx) and the pages after (pdf)
  - Note: the pdf of pages before or after the desired pages aren't created if the desired page is the first or last

Merge.py: Combines the pdfs in the output directory into a single pdf with the same filename as the original
