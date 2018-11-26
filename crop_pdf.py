#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/457207/cropping-pages-of-a-pdf-file

from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger
import glob
import os

pdfs = glob.glob('raw'+os.sep+'*.pdf')
#pdfs = ['raw/'+str(x+1)+'.pdf' for x in xrange(22)]

for pdf in pdfs:
	#print pdf
	with open(pdf, 'rb') as in_f:
		input1 = PdfFileReader(in_f)
		output = PdfFileWriter()

		page = input1.getPage(0)
		#print(page.cropBox.getLowerRight())
		#print(page.cropBox.getLowerLeft())
		#print(page.cropBox.getUpperRight())
		#print(page.cropBox.getUpperLeft())

		#page.mediaBox.lowerRight = (lower_right_new_x_coordinate, lower_right_new_y_coordinate)
		#page.mediaBox.lowerLeft = (lower_left_new_x_coordinate, lower_left_new_y_coordinate)
		#page.mediaBox.upperRight = (upper_right_new_x_coordinate, upper_right_new_y_coordinate)
		#page.mediaBox.upperLeft = (upper_left_new_x_coordinate, upper_left_new_y_coordinate)

	#	page.mediaBox.lowerRight = (595, 0)
	#	page.mediaBox.lowerLeft = (0, 0)
	#	page.mediaBox.upperRight = (595, 842)
	#	page.mediaBox.upperLeft = (0, 842)

		page.mediaBox.lowerRight = (800, 0)
		page.mediaBox.lowerLeft = (850, 360)
		page.mediaBox.upperRight = (300, 650)
		page.mediaBox.upperLeft = (50, 710)

		output.addPage(page)

		with open(pdf.replace('raw','crop'), 'wb') as out_f:
			print pdf.replace('raw','crop')
			output.write(out_f)