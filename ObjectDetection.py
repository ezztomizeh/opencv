import numpy as np
import cv2

def Nothing(x):
    pass

cv2.namedWindow('Tracking')
cv2.createTrackbar('Lower Hue','Tracking',0,255,Nothing)
cv2.createTrackbar('Upper Hue','Tracking',255,255,Nothing)
cv2.createTrackbar('Lower Sat','Tracking',0,255,Nothing)
cv2.createTrackbar('Upper Sat','Tracking',255,255,Nothing)
cv2.createTrackbar('Lower Value','Tracking',0,255,Nothing)
cv2.createTrackbar('Upper Value','Tracking',255,255,Nothing)
Cam = cv2.VideoCapture(1)

while(1):
    seccess , frame = Cam.read()
    HSVImg = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('Frame',frame)
    cv2.imshow('HSV',HSVImg)
    LH = cv2.getTrackbarPos('Lower Hue','Tracking')
    UH = cv2.getTrackbarPos('Upper Hue','Tracking')
    LS = cv2.getTrackbarPos('Lower Sat' , 'Tracking')
    US = cv2.getTrackbarPos('Upper Sat','Tracking')
    LV = cv2.getTrackbarPos('Lower Value','Tracking')
    UV = cv2.getTrackbarPos('Upper Value','Tracking')
    lower = np.array([LH , LS , LV])
    upper = np.array([UH , US , UV])
    Mask = cv2.inRange(HSVImg , lower , upper)
    res = cv2.bitwise_and(frame,frame,mask=Mask)
    cv2.imshow('Rusalt',res)
    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()