# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:47:09 2018

@author: Sagnik
"""

def main():
    print("\n\n Welcome to the Payment System. Put Your Phone on the Device")
    from firebase import firebase
    import serial 
    firebase = firebase.FirebaseApplication('https://sagnikuvce.firebaseio.com/', None)
    ser1 = serial.Serial()
    ser1.baudrate = 9600
    ser1.port = 'COM5'
    ser1.open()
    content = ser1.readline()[:-2]
    data = str(content.decode('utf-8'))
    f = str(data)
    ser1.close()
    table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ','22233344455566677778889999')
    yep = f.translate(table)
    print(yep)
    yolo = int(yep)
    a = f + '/' + 'Name'
    '''
    n = f + '/' + 'Email'
    '''
    b = f + '/' + 'Phone_no'
    c = f + '/' + 'Address'
    d = f + '/' + 'Amount'
    e = f + '/' + 'Money'
    name = firebase.get('/users',a)
    '''
    email = firebase.get('/users',n)
    '''
    print('Hello', name) 
    phone = firebase.get('/users',b)
    add = firebase.get('/users',c)
    amount = firebase.get('/users',d)
    sree = float(amount)
    
    
    
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
        if cv2.waitKey(1)&id == yolo:
            
            cv2.waitKey(6000)
            break
    cam.release()
    cv2.destroyAllWindows()
    cv2.waitKey(0)
    
    
    
    
    
    payment = input('Enter the Payable Amount:   ')
    pay = float(payment)
    to = float(pay)
    hi = sree - pay
    print(hi)
    balance = firebase.get('/uvce','9448608894/Money')
    bal = float(balance)
    ji = bal + to
    print(ji)
    
    
    
    
    
    
    shift = firebase.put('/users',data,{
            'Name': name,
            
            'Phone_no' : phone,
            'Address' : add,
            'Amount' : hi
            })
    print(shift)
    again = firebase.put('/uvce','9448608894',{
            'Name' : 'UVCE',
            'Phone_no': '9448608894',
            'Money' : ji
            })
    print(again)
    print('Thank You for payment :) Have an awesome day', name)
    
    
    
    import smtplib
    s = smtplib.SMTP()
    s.connect('email-smtp.us-east-1.amazonaws.com', 587)
    s.starttls()
    s.login('AKIAILMAFEK3WEWLMR7A', 'Atqb64vJdm05pqz/SlCInpOHgNimXnv5OhoyBNTmEyxx')
    amount = payment
    stri = str(amount)
    suna = str(hi)
    mailID = str('sagniksarkar.me@icloud.com')
    msg = 'From: d.sagnik@campusuvce.in\n'+'To: '+ mailID +'\nSubject: Invoice \n\n' + stri + ' ' + 'has been deducted from your account in UVCE Mall \n' + 'your remaining balance is RS' +' '+suna
    s.sendmail('d.sagnik@campusuvce.in',mailID,msg)
    print('Done')

    
    ser1.close()
    restart = input("New Customer in line? Press y to start the service ")
    if restart == "y" :
        main()
    else:
        exit()
        
main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    