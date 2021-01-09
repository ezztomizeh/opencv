import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
kernal = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernal)
blur = cv.blur(img,(5,5))
gBlur = cv.GaussianBlur(img,(5,5),5)
meddin = cv.medianBlur(img,5)
bilateralFilter = cv.bilateralFilter(img,9,75,75)

titles = ['Orginal' , 'dst' , 'Blur' , 'GaussianBlur' , 'medianBlur' , 'bilateralFilter']
Images = [img,dst,blur,gBlur,meddin,bilateralFilter]

for i in range(6):
    plt.subplot(2,3,i+1) , plt.imshow(Images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])

plt.show()