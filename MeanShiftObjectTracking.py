import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

Cap = cv.VideoCapture('3.mp4')

#! Take the first frame
seccess , frame = Cap.read()
x,y,w,h = 525,517,60,60
#! Set ROI
roi = frame[x: x + h , y: y + w]
# cv.imshow('',roi)
while 1:
    seccess , frame = Cap.read()

    if seccess == True:
        cv.rectangle(frame,(517,525),(390,585),(255),1)
        cv.imshow('video',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    

Cap.release()
cv.destroyAllWindows()