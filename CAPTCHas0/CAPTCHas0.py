#!/usr/bin/env python
'''
CAPTCHas = Completely Automated Public Turing test to tell Computers and Humans Are Same.

Execution:
$ python CAPTCHas0.py test.jpeg
$

Execution will create two files named temp.bmp and data.txt.
temp.bmp: Temporary image file to extract data with tesseract-ocr after image processing with PIL
data.txt: File to save the solved captcha value
'''

from PIL import Image
import os
import sys
import commands

usrimg = Image.open(sys.argv[1])

# Removing background noise.
# Converting the image to greyscale.
captcha = usrimg.convert('1')

# Saving the image as tesseract can read.
captcha.save('temp.bmp', dpi=(200,200))

# Getting the output
commands.getoutput('tesseract temp.bmp data')

# Reading ocr generated output
with open('data.txt', 'r') as data:
    print data.readline().strip()

