import cv2 as cv
import numpy as np

    ###################
    #! Declare images #
    ###################

img = cv.imread('messi5.jpg')
    
    #####################################
    #* Requirements to match a template #
    #####################################

GrayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
Template = cv.imread('messi5_face.jpg')
TemplateGray = cv.cvtColor(Template,cv.COLOR_BGR2GRAY)
football = cv.imread('football.jpg')
Gray = cv.cvtColor(football,cv.COLOR_BGR2GRAY)
hand = cv.imread('hand.jpg')
handGray = cv.cvtColor(hand,cv.COLOR_BGR2GRAY)

    ##########################################
    # TODO: This the way to match a template #
    ##########################################

w , h = TemplateGray.shape[::-1]
res = cv.matchTemplate(GrayImg,TemplateGray,cv.TM_CCORR_NORMED)
threshold = 0.93
loc = np.where(res >= threshold)
print(res)
print(loc)

for pt in zip(*loc[::-1]):
    cv.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0),1)

    ##############################
    #TODO: Matching the football #
    ##############################

w , h = Gray.shape[::-1]
res2 = cv.matchTemplate(GrayImg,Gray,cv.TM_CCOEFF_NORMED)
print(res2)
TH = 0.8
loc = np.where(res2 >= TH)
for pt in zip(*loc[::-1]):
    cv.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0))

    ##########################
    #TODO: Matching the hand #
    #########################

w , h = handGray.shape[::-1]
res3 = cv.matchTemplate(GrayImg,handGray,cv.TM_CCOEFF_NORMED)
TH2 = 0.9
loc = np.where(res3 >= TH2)
for pt in zip(*loc[::-1]):
    cv.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0),1)

    ###################
    #? Showing images #
    ###################

cv.imshow('Orginal',img)
cv.waitKey(0)
cv.destroyAllWindows()