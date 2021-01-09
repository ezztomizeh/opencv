import cv2
from datetime import datetime

Cam = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
save = cv2.VideoWriter('output1.avi',fourcc,20.0,(640,480))
while True:
    seccess , img = Cam.read()
    Gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    if seccess == True:
        Font = cv2.FONT_ITALIC
        width , height = Cam.get(3) , Cam.get(4)
        Text = 'Width: ' + str(int(width)) + '  '
        Text2 = 'Height: ' + str(int(height))
        Date = str(datetime.now())
        cv2.putText(img,Date,(0,460),Font,0.5,(255,255,51),1)
        save.write(img)
        cv2.imshow('Output',img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

Cam.relase()
cv2.destroyAllWindows()