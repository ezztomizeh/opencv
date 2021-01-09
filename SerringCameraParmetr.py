import cv2

Cam = cv2.VideoCapture(1)
Cam.set(3,1280)
Cam.set(4,720)
print(Cam.get(4))
print(Cam.get(3))

while (Cam.isOpened()):
    seccess , img = Cam.read()
    Gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    if seccess == True:
        cv2.imshow('Output',Gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

Cam.release()
cv2.destroyAllWindows()
