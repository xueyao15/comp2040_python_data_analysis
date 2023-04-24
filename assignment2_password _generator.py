'''
Name: Xueyao Wang
Course: DSML Python Essentials
Assignment: Password Generator
Date: 2023-1-10

'''
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?.,-@#$%^&*'

print('Password Generator \n================\n')
         
number = int(input('number of passwords? '))
length = int(input('password length? '))

print('\nHere are your passwords:')
             
for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
