import numpy as np
import cv2

def MouseEevent(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),3,(138,0,69),-1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(0,0,255),5)
        cv2.imshow('Image',img)
    
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        MyImage = np.zeros((255,255,3),np.uint8)
        MyImage[:] = [blue,green,red]
        cv2.imshow('Output',MyImage)
        cv2.imshow('Image',img)

# img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('lena.jpg')
points = []
cv2.imshow('Image',img)
cv2.setMouseCallback('Image',MouseEevent)
cv2.waitKey(0)
