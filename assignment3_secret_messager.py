"""
* Assignment 3
* Xueyao Wang
* Create an encryption program to send and receive secret messages
* Sample output:
*   Please enter an integer key: 3
*   Please enter a message: hi there!!
*   Your new message is: kl wkhuh!!

"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = int(input('Please enter an integer key: '))
message = input('Please enter a message: ')

newMessage = ''
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character

print('Your new message is:  ', newMessage)
