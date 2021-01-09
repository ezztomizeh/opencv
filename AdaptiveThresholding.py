import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png',0)
_,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,10)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,10)

cv.imshow('Output',img)
cv.imshow('TH1',th1)
cv.imshow('TH2',th2)
cv.imshow('TH3',th3)
cv.waitKey(0)