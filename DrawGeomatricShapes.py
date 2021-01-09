import cv2
import numpy as np

# img = cv2.imread('lena.jpg')
img = np.zeros([512,521,3],np.uint8)

#Line
img = cv2.line(img,(0,1),(0,300),(0,255,0),2)
#Arrowed line
img = cv2.arrowedLine(img,(0,0),(255,255),(132,132,152),2)
#Rectangle
img = cv2.rectangle(img,(255,255),(300,300),(255,0,0),1)
#Circle
img = cv2.circle(img,(122,213),50,(0,255,0),5)
#Put text
img= cv2.putText(img,'openCV',(123,55),cv2.FONT_ITALIC,1,(0,0,51),5)

cv2.imshow('Orginal - 0',img)
Key = cv2.waitKey(0)

if Key == ord('q'):
    cv2.destroyAllWindows()