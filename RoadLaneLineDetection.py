import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

    ##############
    #! Functions #
    ##############

def roi(img,vertices):
    mask = np.zeros_like(img)
    # ChannelCount = img.shape[2]
    MaskMatchedColor = 255
    cv.fillPoly(mask,vertices,MaskMatchedColor)
    MaskedImage = cv.bitwise_and(img,mask)
    return MaskedImage

def Draw(img,lines):
    img = np.copy(img)
    LineImage = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(LineImage,(x1,y1),(x2,y2),(255,0,0),5)
    img = cv.addWeighted(img,0.8,LineImage,1,0.0)
    return img

    ###############
    #! The script #
    ###############

img = cv.imread('road.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

print(img.shape)
height = img.shape[0]
width = img.shape[1]

ROI = [
    (0,height),
    (width/2 , height/2),
    (width , height)
]

Gary = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
Edges = cv.Canny(Gary,100,200,apertureSize=3)
CropedImage = roi(Edges,np.array([ROI], np.int32))
# GrayCroped = cv.cvtColor(CropedImage,cv.COLOR_RGB2GRAY)
lines = cv.HoughLinesP(CropedImage,4,np.pi / 60,100,
                        np.array([]),minLineLength=40,maxLineGap=25)
img2 = Draw(img,lines)

cv.imshow('Orginal',img)
cv.imshow('Canny',img2)
cv.waitKey(0)