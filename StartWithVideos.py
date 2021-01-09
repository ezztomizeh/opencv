import cv2

webCam = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
save = cv2.VideoWriter('output1.avi',fourcc,20.0,(640,480))
while (True):
    scess , img = webCam.read()
    if scess == True:
        cv2.imshow('Video',img)
        save.write(img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
