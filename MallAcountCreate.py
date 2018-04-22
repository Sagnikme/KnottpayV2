from firebase import firebase
firebase = firebase.FirebaseApplication('https://knottpay-190817.firebaseio.com/', None)
name = input('Enter the Mall Name: ')
phone = input('Enter the Mall Phone Number: ')
money = input('Enter the amount(above Rs 1) to start the account ')
resultz = firebase.patch('/Mall'+'/'+ name,{
    'Name' : name,
    'Phone_no' : phone,
    'Money' : money
    })
print(resultz)
