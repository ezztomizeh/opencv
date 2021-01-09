import cv2 as cv
import numpy as np

    ###################
    #* Read an video #
    ###################
    
video = cv.VideoCapture(0)
seccess , img1 = video.read()
seccess , img2 = video.read()


    ################
    #! Run a video #
    ################

while True:


    ####################
    #? It's take 2 var #
    ####################

    #seccess , img = video.read()
    diff = cv.absdiff(img1,img2)
    gray = cv.cvtColor(diff,cv.COLOR_RGB2GRAY)
    blur = cv.GaussianBlur(gray,(5,5),0)
    _ , tresh = cv.threshold(blur,20,255,cv.THRESH_BINARY)
    ditled = cv.dilate(tresh,None,iterations=3)
    cv.imshow('D',ditled)
    con , hir = cv.findContours(ditled,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    ###################################################
    # TODO: Draw rectangles and detecte who is moving #
    ###################################################

    for conutor in con:
        if cv.contourArea(conutor) < 10000:
            continue
        cv.drawContours(img1,con,-1,(0,255,0),2) 

    # for contour in con:
    #     (x , y , w , h) = cv.boundingRect(contour)
    #     if cv.contourArea(contour) < 10000:
    #         continue
    #     cv.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),3)
    #     cv.putText(img1,'status: {}'.format('Movment') , (10,20),cv.FONT_HERSHEY_COMPLEX,
    #                                                     0.5,(255,0,0),2)                           

    cv.imshow('Video',img1)
    img1 = img2
    ret , img2 = video.read()

    ####################
    #TODO: Keys events #
    ####################

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()