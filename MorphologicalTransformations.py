import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("smarties.png" , cv.IMREAD_GRAYSCALE)
_ , mask = cv.threshold(img,220,255,cv.THRESH_BINARY_INV)
kernal = np.ones((2,2),np.uint8)
daliton = cv.dilate(mask,kernal,iterations=4)
erotion = cv.erode(mask,kernal,iterations=1)
opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernal)
closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernal)
title = ['Image','Mask' , 'dilation' , 'erotion','opening','closing']
image = [img,mask,daliton,erotion,opening,closing]

for i in range(6):
    plt.subplot(2,3,i+1) , plt.imshow(image[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()