import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg')
layer = img.copy()
gb = [layer]

for i in range(5):
    layer = cv.pyrDown(layer)
    gb.append(layer)
    #! cv.imshow(str(i),layer)

layer = gb[-1]
cv.imshow('Upper',layer)

lr = [layer]

for i in range(5,0,-1):
    Gx = cv.pyrUp(gb[i])
    La = cv.subtract(gb[i-1],Gx)
    cv.imshow(str(i),La)

cv.waitKey(0)