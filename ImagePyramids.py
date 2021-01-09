import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg')


#########################
Pd = cv.pyrDown(img)    #
Pd2 = cv.pyrDown(Pd)    #
Pd3 = cv.pyrDown(Pd2)   #
Pd4 = cv.pyrDown(Pd3)   #
#########################
Pp = cv.pyrUp(Pd)
cv.imshow('Orginal Image',img)
cv.imshow('Pp',Pp)

#########################
# cv.imshow('Pd',Pd)    #
# cv.imshow('Pd2',Pd2)  #
# cv.imshow('Pd3',Pd3)  #
# cv.imshow('Pd4',Pd4)  #
#########################

cv.waitKey(0)
cv.destroyAllWindows()