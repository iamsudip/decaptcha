#!/usr/bin/env python
'''
CAPTCHas = Completely Automated Public Turing test to tell Computers and Humans Are Same.
'''

#import urllib2
from PIL import Image
#import StringIO
import sys

#opener = urllib2.build_opener()
#usrdata = opener.open('http://just4today.net/username.php').read()
#usrimg = Image.open(StringIO.StringIO(usrdata))
usrimg = Image.open(sys.argv[1])
usrimg.show()    # Previewing fresh unalterd image.

# Removing background noise.
# Converting the image to greyscale.
captcha = usrimg.convert('L', (.4, .4, .4, 0))
captcha.show()    # Previewing greyscale image.

# Removing all shades lighter than a given value(107)
for x in range(captcha.size[1]):
    for y in range(captcha.size[0]):
        if captcha.getpixel((y,x)) > 107:
            captcha.putpixel((y,x),255)
captcha.show()    # Previewing final image
