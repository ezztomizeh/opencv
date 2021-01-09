import numpy as np
import cv2

def empty(x):
    pass

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('Image')
cv2.createTrackbar('Blue','Image',0,255,empty)
cv2.createTrackbar('Green','Image',0,255,empty)
cv2.createTrackbar('Red','Image',0,255,empty)
switch = '1: ON \n 2: OFF'
cv2.createTrackbar(switch,'Image',0,1,empty)
while (1):
    cv2.imshow('Image',img)
    Key = cv2.waitKey(1) & 0xFF
    if Key == 27:
        break
    elif Key == ord('s'):
        cv2.imwrite('SS.jpg',img)
    Blue = cv2.getTrackbarPos('Blue','Image')
    Green = cv2.getTrackbarPos('Green','Image')
    Red = cv2.getTrackbarPos('Red','Image')
    Switch = cv2.getTrackbarPos(switch,'Image')
    if Switch == 0:
        img[:] = 0
    else:
        img[:] = [ Blue, Green, Red]
    print(Blue,Green,Red)
cv2.destroyAllWindows()