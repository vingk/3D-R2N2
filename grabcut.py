#!/usr/bin/env python
'''
===============================================================================
Interactive Image Segmentation using GrabCut algorithm.

This sample shows interactive image segmentation using grabcut algorithm.

USAGE:
    python grabcut.py <filename>

README FIRST:
    Two windows will show up, one for input and one for output.

    At first, in input window, draw a rectangle around the object using
mouse right button. Then press 'n' to segment the object (once or a few times)
For any finer touch-ups, you can press any of the keys below and draw lines on
the areas you want. Then again press 'n' for updating the output.

Key '0' - To select areas of sure background
Key '1' - To select areas of sure foreground
Key '2' - To select areas of probable background
Key '3' - To select areas of probable foreground

Key 'n' - To update the segmentation
Key 'r' - To reset the setup
Key 's' - To save the results
===============================================================================
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv
import sys

BLUE = [255,0,0]        # rectangle color
RED = [0,0,255]         # PR BG
GREEN = [0,255,0]       # PR FG
BLACK = [0,0,0]         # sure BG
WHITE = [255,255,255]   # sure FG

DRAW_BG = {'color' : BLACK, 'val' : 0}
DRAW_FG = {'color' : WHITE, 'val' : 1}
DRAW_PR_FG = {'color' : GREEN, 'val' : 3}
DRAW_PR_BG = {'color' : RED, 'val' : 2}

# setting up flags
rect = (0,0,1,1)
drawing = False         # flag for drawing curves
rectangle = False       # flag for drawing rect
rect_over = False       # flag to check if rect drawn
rect_or_mask = 100      # flag for selecting rect or mask mode
value = DRAW_FG         # drawing initialized to FG
thickness = 3           # brush thickness


if __name__ == '__main__':

    # print documentation
    print(__doc__)

    # Loading images
    if len(sys.argv) == 2:
        filename = sys.argv[1] # for drawing purposes
    else:
        print("No input image given, so loading default image, ../data/lena.jpg \n")
        print("Correct Usage: python grabcut.py <filename> \n")
        filename = '../data/lena.jpg'

    img = cv.imread(filename)
    img2 = img.copy()                               # a copy of original image
    mask = np.zeros(img.shape[:2],dtype = np.uint8) # mask initialized to PR_BG
    output = np.zeros(img.shape,np.uint8)           # output image to be shown

    width, height =  img2.shape[:2]
    rect = (0,0, width-1, height-1)
    # input and output windows
    cv.namedWindow('output')
    cv.namedWindow('input')
    #cv.setMouseCallback('input',onmouse)
    cv.moveWindow('input',img.shape[1]+10,90)

    print(" Instructions: \n")
    print(" Draw a rectangle around the object using right mouse button \n")

    bgdmodel = np.zeros((1,65),np.float64)
    fgdmodel = np.zeros((1,65),np.float64)
    cv.grabCut(img2,mask,rect,bgdmodel,fgdmodel,1,cv.GC_INIT_WITH_RECT)
    rect_or_mask = 1
    mask2 = np.where((mask==1) + (mask==3),255,0).astype('uint8')
    output = cv.bitwise_and(img2,img2,mask=mask2)


    cv.imshow('output',output)
    cv.imshow('input',img)
    k = cv.waitKey(10000)
    if k == 27:
        cv.destroyAllWindows()

