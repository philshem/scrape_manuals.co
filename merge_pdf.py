#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/3444645/merge-pdf-files

from PyPDF2 import PdfFileMerger
import glob
import os
import config

pdfs = glob.glob('crop'+os.sep+'*.pdf')
#pdfs = ['crop/'+str(x+1)+'.pdf' for x in xrange(22)]

#print sorted(pdfs)

merger = PdfFileMerger()

for pdf in sorted(pdfs):
	print pdf
	merger.append(open(pdf, 'rb'))

merger.write('full_manual.pdf')
