import cv2
import time

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer\\trainningData.yml")
id = 0
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)
time.sleep(2)
cv2.startWindowThread()
while True:
    ret,frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h),(255,255,255),1)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        cv2.putText(frame,str(id),(x,y+h),fontface, fontscale, fontcolor)
        
    cv2.imshow('Detection and Identification', frame)
    if cv2.waitKey(1)&id == 96739822:
        
        cv2.waitKey(6000)
        break

cam.release()
cv2.destroyAllWindows()
cv2.waitKey(0)
