"""
Program to take video as input and produce video frames
"""

import cv2

#function to create frames from the video
def createFrames(inputFile, outputFolder):
  vidcap = cv2.VideoCapture(inputFile)
  success,image = vidcap.read()
  image2 = cv2.resize(image,(127,127))
  count = 0
  success = True
  while success:
    cv2.imwrite(outputFolder+"%d.jpg" % count, image2)     # save frame as JPEG file
    success,image = vidcap.read()
    #print 'Read a new frame: ', success
    count += 1

if __name__==main():
  #example file names
  inputFile = 'Video2.MOV'
  outputFolder = "/home/robotics/Downloads/imgs_raw/"
  createFrames(inputFile, outputFolder)
