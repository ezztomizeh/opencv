import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg',cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img,cv.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
sobelY = cv.Sobel(img,cv.CV_64F,0,1,ksize=3)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCom = cv.bitwise_or(sobelX,sobelY)

Titles = ['Orginal','Laplacian']
Images = [img,lap]

# for i in range(2):
#     plt.subplot(1,2,i+1),plt.imshow(img,'gray')
#     plt.title(Titles[i])
#     plt.xticks([]) , plt.yticks([])

cv.imshow('Orginal',img)
cv.imshow('Laplacian',lap)
cv.imshow('SobelX',sobelX)
cv.imshow('SobelY',sobelY)
cv.imshow('SobelCom',sobelCom)
# plt.show()
cv.waitKey(0)