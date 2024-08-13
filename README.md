# Intro
Small utility to read text from images, written in python.
This is a wrapper over open source text recognition (OCR) engine [Tesseract](https://github.com/tesseract-ocr/tesseract). 

# Input Parameters

## Canvas Scope 
The canvas scope defines the area within which we should read the text.
The input for this will be the points of the rectangle area.
Canvas scope: (x, y, width, height)


# Setup

(Only for MacOS, modify the setup steps accordingly for other OS')

## Tesseract 

`brew install tesseract`


# Supported Scope

This only works for English text right now. 

To be added:
- Canvas scope exception handling
- Arabic conversion
- Russian conversion