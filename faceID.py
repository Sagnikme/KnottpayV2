# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:55:20 2018

@author: Sagnik
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 00:14:40 2018

@author: Sagnik
"""
### Libraries used ###
import serial
import cv2
import time
import os
import numpy as np
import dropbox
from PIL import Image
import shutil

### PORT Starts here ###
print("\n\n Welcome to the Face Recognition part of the Payment System. Put Your Phone on the Device")

ser1 = serial.Serial()
ser1.baudrate = 9600
ser1.port = 'COM5'
ser1.open()
content = ser1.readline()[:-2]
data = str(content.decode('utf-8'))
f = str(data)
print(f)
ser1.close()

table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ','22233344455566677778889999')
yep = f.translate(table)
print(yep)
revTable = str.maketrans('22233344455566677778889999','ABCDEFGHIJKLMNOPQRSTUVWXYZ')
yass = f.translate(revTable)
print(yass)
new = str(yass)
### Detector Starts Here ###
home_dir = (r'''C:\Users\Sagnik\Desktop\Project\dataSet''')   
if not os.path.isdir(home_dir):
    os.makedirs(home_dir)
    


faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
time.sleep(2)
cv2.startWindowThread()
id = input("Enter the ID: ")
print ('Please wait as your face is being scanned ', id)
sampleNo = 0
while True:
    ret,frame = cam.read()
    gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        sampleNo = sampleNo+1
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNo)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),(x+w, y+h),(255,255,255),1)
        cv2.waitKey(600)
    cv2.imshow("Face", frame)
    cv2.waitKey(1)
    if(sampleNo>50):
        break 

cam.release()
cv2.destroyAllWindows()
cam.release()
cv2.destroyAllWindows()
cv2.waitKey(0)
### Trainner Starts Here ###

if not os.path.isdir(home_dir):
    os.makedirs(home_dir)


recognizer=cv2.face.LBPHFaceRecognizer_create();
path= r'dataSet'


def getImagesWithID(path):
	imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
	faces=[]
	IDs=[]
	for imagePath in imagePaths:
		faceImg=Image.open(imagePath).convert('L');
		faceNp=np.array(faceImg,'uint8')
		ID=int(os.path.split(imagePath)[-1].split('.')[1])
		faces.append(faceNp)
		print (ID)
		IDs.append(ID)
		cv2.imshow("training",faceNp)
		cv2.waitKey(400)
	return IDs,faces

Ids,faces=getImagesWithID(path)
recognizer.train(faces,np.array(Ids))
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()
### Delete the dataset###
shutil.rmtree(home_dir, ignore_errors=True)
### Dropbox YML Upload ###
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'f_hjRlTkx0AAAAAAAAADvBfY5hiVPot6dJqgrMiYNrG1K1NJGUhzkklBLWmg7ITE'
    transferData = TransferData(access_token)

    file_from = 'recognizer/trainningData.yml'
    file_to = '/FaceID'+'/'+new+'/'+'trainningData.yml'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("uploaded")

if __name__ == '__main__':
    main()
                 
             
             
             
             
              
              









    
    
    
    
        
        
        
        
    
    
   
       





### Detection Ends Here ###





