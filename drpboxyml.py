# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 05:07:35 2018

@author: Sagnik
"""
def main():
    print("\n\n Welcome to the Payment System. Put Your Phone on the Device")
    import dropbox
    import urllib.request
    import serial
    from firebase import firebase
     
    firebase = firebase.FirebaseApplication('https://knottpay-190817.firebaseio.com/', None)
    ser1 = serial.Serial()
    ser1.baudrate = 9600
    ser1.port = 'COM5'
    ser1.open()
    content = ser1.readline()[:-2]
    data = str(content.decode('utf-8'))
    f = str(data)
    ser1.close()
    table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ','22233344455566677778889999')
    revTable = str.maketrans('22233344455566677778889999','ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    yass = f.translate(revTable)
    print(yass)
    yep = f.translate(table)
    print(yep)
    yolo = int(yep)
    print(yolo)
    new = str(yass)
    access_token = 'f_hjRlTkx0AAAAAAAAADvBfY5hiVPot6dJqgrMiYNrG1K1NJGUhzkklBLWmg7ITE'
    dbx = dropbox.Dropbox(access_token)
    url = 'https://www.dropbox.com/sh/2jmlwvpx0jie85y/AABGIDaixVDt9pEM76sX_KaUa'+'/'+new+'/trainningData.yml?raw=1'
    u = urllib.request.urlopen(url)
    data = u.read()
    u.close()  
    with open('traindata/trainningData.yml', "wb") as f :
        f.write(data)
    print("Done")
    restart = input("New Customer in line? Press y to start the service ")
    if restart == "y" :
        main()
    else:
        exit()
        
main()