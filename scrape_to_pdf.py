#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python

import config

import pdfkit
import os

urlbase = config.urlbase

for x in xrange(config.min_page-1,config.max_page-1):
	url = urlbase+str(x+1)
	print(url)
	pdfkit.from_url(url, 'raw'+os.sep+str(x+1).zfill(4)+'.pdf')
