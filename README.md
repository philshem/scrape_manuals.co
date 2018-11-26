# scrape_manuals.co
+ Python web scraper for automobile workshop repair manuals from https://manuals.co
+ Generates one pdf `full_manual.pdf` by converting individual html pages to pdf, cropping the manual page, and merging individual pdfs into one.

Steps:

0. Download code and create folders `raw/` and `crop/`

1. Update `config.py` for your URL and min and max page

2. Run web scraping code. Update config.py if you can't get all the pages in one shot
 
   `$ python scrape_to_pdf.py`

3. Run `crop_pdf.py` to get pdfs with the correct dimensions. The individual cropped files are in directory `crop/`

   `$ python crop_pdf.py`
   
4. Run `merge_pdf.py` to combine individual pdfs into one output file: `full_manual.pdf`

   `$ python merge_pdf.py`
   
99. Check the contents of `full_manual.pdf` and if satisfied, manually delete individual pdf files in the temp folders `raw/` and `crop/`
   
   
------------------

Requires standard Python and a couple non-standard libraries: [pdfkit](https://pypi.org/project/pdfkit/) and [PyPDF2](https://pypi.org/project/PyPDF2/).

------------------

No warranty. For personal and experimental use. Public domain license. 
