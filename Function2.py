'''
----------------------- LOGIC GATES ----------------------
AND GATE :-
    0 AND 0 = 0 , 0 AND 1 = 0 , 1 AND 0 = 0 , 1 AND 1 = 1
    CV2.BITWISE_AND(SRC1,SCR2)
OR GATE :-
    0 OR 0 = 0 , 1 OR 0 = 1 , 0 OR 1 = 1 , 1 OR 1 = 1
    CV2.BITWISE_OR(SRC1,SCR2)
NOT GATE :-
    IT'S TAKE ONE ARG*
    NOT 0 = 1 , NOT 1 = 0
    CV2.BITWISE_NOT(SRC)
XOR GATE :-
    0 XOR 0 = 0 , 1 XOR 1 = 0 , 0 XOR 1 = 1 , 1 XOR 0 = 1
    CV2.BITWISE_XOR(SRC1,SRC2)
'''

import numpy as np
import cv2

img1 = np.zeros((400,600,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread('wh.png')
# bitAnd = cv2.bitwise_and(img1,img2)
# bitOr = cv2.bitwise_or(img1,img2)
# bitNot = cv2.bitwise_not(img1)
bitXor = cv2.bitwise_xor(img2,img1)
#Show
cv2.imshow('Image #1' , img1)
cv2.imshow('Image #2' , img2)
cv2.imshow('Rusalt - bitAnd' , bitXor)
cv2.waitKey(0)
cv2.destroyAllWindows()
