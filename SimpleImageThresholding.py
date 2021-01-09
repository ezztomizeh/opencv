import cv2 as cv
import numpy as np

img = cv.imread('gradient.png',0)
_ , th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
_ , th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_ , th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
_ , th4 = cv.threshold(img,200,255,cv.THRESH_TOZERO)
_ , th5 = cv.threshold(img,200,255,cv.THRESH_TOZERO_INV)

cv.imshow('Output',img)
# cv.imshow('Image',th1)
# cv.imshow('Image',th2)
# cv.imshow('Image',th3)
# cv.imshow('Image',th4)
cv.imshow('Image',th5)

cv.waitKey(0)
cv.destroyAllWindows()