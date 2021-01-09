import cv2 as cv
import numpy as np

img = cv.imread('road.jpg')
# img = cv.resize(img,(500,500))
imgGray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)

edges = cv.Canny(img,50,150,apertureSize=3)
lines = cv.HoughLinesP(edges,1,np.pi / 180,100,minLineLength=100,maxLineGap=10)

for line in lines :
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),3)

cv.imshow('Orginal',img)
cv.imshow('canny',edges)
cv.waitKey(0)
cv.destroyAllWindows()