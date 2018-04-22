# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 23:25:50 2018

@author: Sagnik
"""
from firebase import firebase
import serial

ip = input("Type R for recharge or N for new connection ")




if ip == "N":
    ser1 = serial.Serial()
    ser1.baudrate = 9600
    ser1.port = 'COM5'
    ser1.open()
    content = ser1.readline()[:-2]
    data = str(content.decode('utf-8'))
    f = str(data)

    print("\n\n Welcome to the Payment System New User  ")
    
    
    
    name = input('Enter  the customer Name:  ')
    email = input('Enter the customer Email ID: ')
    address = input('Enter the address:  ')
    phone_no = input('Enter the phone Number:  ')
    amount = input('Enter the Starting balance:  ')
    firebase = firebase.FirebaseApplication('https://knottpay-190817.firebaseio.com/', None)
    result = firebase.patch('/Users'+'/'+ data + '/',{
               'Name' : name,
               'Email' : email,
               'Address': address,
               'Phone_no':phone_no,
               'Amount':amount
               })
       
    print(result)
    ser1.close()
elif ip == "R":
    
    print("\n\nPut Your Phone on the Device for Recharge  ")
    ser1 = serial.Serial()
    ser1.baudrate = 9600
    ser1.port = 'COM5'
    ser1.open()
    content = ser1.readline()[:-2]
    data = str(content.decode('utf-8'))
    f = str(data)

    firebase = firebase.FirebaseApplication('https://knottpay-190817.firebaseio.com/', None)
    
    
    a = f + '/' + 'Name'
    n = f + '/' + 'Email'
    b = f + '/' + 'Phone_no'
    c = f + '/' + 'Address'
    d = f + '/' + 'Amount'
    e = f + '/' + 'Money'
    
    
    name = firebase.get('/Users',a)
    print('Hello', name)
    rec = input('Enter the amount you want to recharge  ')
    email = firebase.get('Users',n)
    
    if name is None :
        exit()
    phone = firebase.get('/Users',b)
    add = firebase.get('/Users',c)
    amount = firebase.get('/Users',d)
    sree = float(amount)
    pay = float(rec)
    hi = sree + pay
    
    
    
    shift = firebase.put('/Users',data,{
            'Name': name,
            'Email': email,
            'Phone_no' : phone,
            'Address' : add,
            'Amount' : hi
            })
    print('Thank You for recharge :) Have an awesome day', name)
    print('Your New Account Balance is ', hi )
    ser1.close()
    
    
    
    
    
   
   
    