import cv2

img = cv2.imread('lena.jpg')
cv2.imshow('Output',img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('lenaCopy.jpg',img)
    cv2.imshow('Output',img)
    cv2.waitKey(0)