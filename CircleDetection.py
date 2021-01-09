import cv2 as cv
import numpy as np

img = cv.imread('shapes.png')
output = img.copy()
gray = cv.cvtColor(output,cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray,5)
circle = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,500,
                        param1=50 , param2= 30 , minRadius= 0 , maxRadius=0)

DetecedCircle = np.uint16(np.around(circle))

for (x,y,r) in DetecedCircle[0,:] :
    cv.circle(output,(x,y),r,(0),2)

cv.imshow('Output',output)
cv.waitKey(0)
cv.destroyAllWindows()