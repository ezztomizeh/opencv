import cv2 as cv
import numpy as np

# img = cv.imread('face.jpg')
video = cv.VideoCapture(0)

while True:
    face = cv.CascadeClassifier('face.xml')
    eye = cv.CascadeClassifier('eye.xml')
    _ , img = video.read()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    Faces = face.detectMultiScale(img,1.1,4)
    Eyes = eye.detectMultiScale(img)

    for (x,y,w,h) in Faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

    for (x,y,w,h) in Eyes:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    cv.imshow('Orginal',img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    
cv.destroyAllWindows()