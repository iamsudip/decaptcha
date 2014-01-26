CAPTCHas scripts
================

Completely Automated Public Turing test to tell Computers and Humans Are Same :p

CAPTCHas1.py - Flipkart.com captcha solver
------------------------------------------

Dependencies:: 

    libleptonica, libtesseract3, libwebp2, tesseract-ocr,
    tesseract-ocr-eng, tesseract-ocr-equ, tesseract-ocr-osd
    
For debian user::

    $ sudo apt-get install tesseract-ocr

This will install all the dependencies.

Run it as ::

    $ python CAPTCHas1.py test1.jpeg

The solved captcha data will be saved into same as pwd in data.txt. (y)

