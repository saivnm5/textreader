# Intro
Small utility to read text from images, written in python. 

We will be able to define parameters to extract only the text we need.

# Parameters

Canvas Scope Parameter
The first set of parameters will be called the canvas scope.
The canvas scope defines the area within which we should read the text.
The input for this will be the points of the rectangle area.
Canvas scope: (x, y, width, height)

Selective Text
We may just want the title (or the biggest sized text) or the entire text content. 
This is also an input, where user has to select either: 
"title" or "fulltext" as an option.


# Setup

brew install tesseract


# Supported Scope

This only works for English text right now. 
Also, the canvas scope needs to be proper. Exception handling is yet to be added.