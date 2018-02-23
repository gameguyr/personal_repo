#!/usr/bin/python
########################
# TITLE: pdf_v1
# AUTHOR: russell lego
# DATE: 2018-01-24
# PURPOSE:
########################


#################################
# Importing Modules
#################################
import PyPDF2

#################################
# Defining Constants
#################################


#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################


#################################
# Performing Work
#################################

import PyPDF2
pdfFileObj = open('test_1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()
