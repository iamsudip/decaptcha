#!/usr/bin/env python
'''
CAPTCHas = Completely Automated Public Turing test to tell Computers and Humans Are Same.
Flipkart.com - the online mega store's captchas are not solid.
Flipkart.com captcha solver.
'''

from PIL import Image
import sys
import commands

usrimg = Image.open(sys.argv[1])

# Removing background noise.
# Converting the image to greyscale.
captcha = usrimg.convert('L', (.4, .4, .4, 0))

# Removing all shades lighter than a given value(107)
for x in range(captcha.size[1]):
    for y in range(captcha.size[0]):
        if captcha.getpixel((y,x)) > 400:
            captcha.putpixel((y,x),255)

# Saving the image as tesseract can read.
captcha.save('temp.bmp', dpi=(200,200))

# Getting the output
commands.getoutput('tesseract temp.bmp data')
