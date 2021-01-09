import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg',-1)
img2 = cv.cvtColor(img,cv.COLOR_BGR2RGB)

cv.imshow("Output",img)
plt.imshow(img2)
plt.show()
cv.waitKey(0)