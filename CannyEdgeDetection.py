import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Images
img = cv.imread('messi5.jpg',0)

#Empty Function
def a(f):
    pass

#NamedWindow
cv.namedWindow('Trackbar')
TH1 = cv.createTrackbar('TH1','Trackbar',0,1000,a)
TH2 = cv.createTrackbar('TH2','Trackbar',0,1000,a)

while True:
    TH1Val = cv.getTrackbarPos('TH1','Trackbar')
    TH2Val = cv.getTrackbarPos('TH2','Trackbar')
    canny = cv.Canny(img,TH1Val,TH2Val)
    cv.imshow('',canny)
    print(TH1Val,TH2Val)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()