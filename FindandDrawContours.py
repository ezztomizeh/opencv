import cv2 as cv
import numpy as np

def empty(s):
    return

img = cv.imread('Shapes.png')
grayIMG = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny = cv.Canny(img,127,255)
con , hir = cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    #print(str(len(con)))
cv.drawContours(img,con,-2,(204,0,0),3)

    # cv.imshow('Orginal',img)
    # cv.imshow('Gray',grayIMG)
cv.imshow('Canny',canny)
cv.imshow('',img)
cv.waitKey(0)

cv.destroyAllWindows()