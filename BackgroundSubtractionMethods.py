import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)
fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False,varThreshold=100)
# fgbg2 = cv. #cv.createBackgroundSubtractorMOG2()
while True:
    _ , frame = video.read()

    if frame is None:
        break

    fgmask = fgbg.apply(frame)
    fgmask = cv.cvtColor(fgmask,cv.COLOR_BGR2GRAY)
    con = cv.findContours(fgmask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for cons in con:
        cv.drawContours(fgmask,con,-1,(255))
    # fgmask2 = fgbg2.apply(frame)

    cv.imshow('',fgmask)
    keybord = cv.waitKey(30)

    if keybord == 'q' or keybord == 27:
        break

video.release()
cv.destroyAllWindows()