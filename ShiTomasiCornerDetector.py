import cv2 as cv
import numpy as np

img = cv.imread('pic1.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,(0,0,255),-2)

cv.imshow('',img)
cv.waitKey(0)