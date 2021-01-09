import cv2 as cv
import numpy as np

    #######################
    #! Delcare the images #
    #######################

img = cv.imread('Shapes.jpg')
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
blur = cv.medianBlur(gray,5)

    ###########################
    #TODO: Detecte the shapes #
    ###########################

_ , thersh = cv.threshold(gray,240,255,cv.THRESH_BINARY)
con , _ = cv.findContours(thersh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

        ############################################
        #* For loop to draw and detecte each shpae #
        #############################################
         #? Epsilon is the approximation accuracy   #
         #? Closed is mean the shpaes close or not  #
         #? approxPolyDP is going to polygon curves #
         ############################################

def text(text):
    cv.putText(img,str(text),(x+3,y-3),cv.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)

for contour in con:
    approx = cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
    x , y , w , h = cv.boundingRect(approx)
    ass = float(w)/h

    if cv.contourArea(contour) > 500 :
        cv.drawContours(img,[approx],0,(0,0,102),3)
        if len(approx) == 3 : text('Triangle')
        elif len(approx) == 4 and ass >= 0.95 and ass <= 1.05 : text('Squre')
        elif len(approx) == 4 and w != h : text('Rectangle')
        elif len(approx) == 5 : text('Pentagon')
        elif len(approx) == 6 : text('Hexagon')
        elif len(approx) == 10 : text('Star')

    ################################
    #     TODO: Detece Circles     #
    ################################

CircleDetection = cv.HoughCircles(blur,cv.HOUGH_GRADIENT,1,
                                 1000,param1=50,param2=30,minRadius=0,maxRadius=0)

DetectedCircle = np.uint16(np.around(CircleDetection))
for (x,y,r) in DetectedCircle[0,:]:
    cv.circle(img,(x,y),r,(0,0,102),2)
    text('Circle')

    ####################
    #? Show the images #
    ####################

cv.imshow('Orginal',img)
cv.waitKey(0)
cv.destroyAllWindows()