import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
#panel = np.zeros([100, 700], np.uint8)
#cv2.namedWindow('panel')
 
def nothing(x):
    pass
 
def biggestContourI(contours):
    maxVal = 0
    maxI = None
    for i in range(0, len(contours) - 1):
        if len(contours[i]) > maxVal:
            cs = contours[i]
            maxVal = len(contours[i])
            maxI = i
    return maxI

cap = cv2.VideoCapture('/home/robotics/Documents/code/bgslibrary/dataset/Video2.MOV')

count = 0
while True:
    _, frame = cap.read()
    count += 1

    e_r,e_c,channels = frame.shape

    roi = frame[0: e_r, 0: e_c]
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
 
    l_h = 0
    u_h = 179
    l_s = 0
    u_s = 255
    l_v = 0
    u_v = 120
 
    lower_green = np.array([l_h, l_s, l_v])
    upper_green = np.array([u_h, u_s, u_v])
 
    mask = cv2.inRange(hsv, lower_green, upper_green)
    #mask_inv = cv2.bitwise_not(mask)


    for i in range(e_r):
        for j in range(e_c):
            if mask[i,j] == 0:
                frame[i,j] = [255,255,255]  

    image2 = cv2.resize(frame,(127,127))
    
    cv2.imshow('img', image2)
    #cv2.imshow('flt', mask)
    cv2.imwrite('/home/robotics/Downloads/imgs/'+str(count)+'.jpg',image2)

 
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
 
cap.release()
cv2.destroyAllWindows()
