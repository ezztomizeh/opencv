import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def eventClick(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' , ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , ' + str(y)
        cv2.putText(img,strXY,(x,y),font,0.5,(52,97,235))
        cv2.imshow('Image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img,strXY,(x,y),font,0.5,(0,255,0))
        cv2.imshow('Image',img)

img = cv2.imread('lena.jpg')
cv2.imshow('Image',img)
cv2.setMouseCallback('Image',eventClick)
cv2.waitKey(0)