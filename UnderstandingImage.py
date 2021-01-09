import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

    #########################
    #! Declaring the images #
    #########################
    #? Create a black image #
    #########################

img = np.zeros((200,200),np.uint8)
lena = cv.imread('lena.jpg')

    #########################################
    # TODO: Find the histogram by matlotlib #
    #########################################

cv.rectangle(img,(0,100),(200,200),(255,255,255),-1)
cv.rectangle(img,(0,50),(100,100),(204,204,0),-1)
# plt.hist(lena.ravel(),256,[0,256])

    #########################
    # TODO: Split BGR Value #
    #########################

b , g , r = cv.split(lena)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

    #######################
    #* Showing the images #
    #######################

cv.imshow('Orginal',lena)
# cv.imshow('b',b)
# cv.imshow('g',g)
# cv.imshow('r',r)
plt.show() # Show for plt
cv.waitKey(0)
cv.destroyAllWindows()