#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python

import config

import pdfkit
import os
import glob
from random import randint
from time import sleep
import datetime
from interruptingcow import timeout

urlbase = config.urlbase

existing_pdfs = glob.glob('raw'+os.sep+'*.pdf')
#print existing_pdfs
#exit(0)

for x in xrange(config.min_page,config.max_page):
	url = urlbase+str(x)
	pdf_file = 'raw'+os.sep+str(x).zfill(4)+'.pdf'

	if not os.path.exists(pdf_file):
		print(datetime.datetime.now())
		try:
			with timeout(60*1, exception=RuntimeError):
				while True:
					pdfkit.from_url(url, pdf_file)
					print('new pdf:',pdf_file)
					sleep(randint(5,35))

		except RuntimeError:
			print('taking a small break')
			sleep(60*1)
			pass
		except:
			print('taking a big break')
			sleep(60*10)
			pass
	else:
		print('exists:',pdf_file)

