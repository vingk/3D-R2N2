import numpy as np
import cv2 as cv

img = cv.imread('chair.jpg')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
fgmask = fgbg.apply(img)
cv.imshow('frame',fgmask)
k = cv.waitKey(30) & 0xff
cv.destroyAllWindows()
