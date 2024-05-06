
# coding: UTF-8

# password_generator_for_multiple.py

from random import choice
import os, string

os.system ('cls')

quantity_of_passwords = int (input ('Quantity of passwords: '))
size_of_password = int (input ('Dígits: '))

characters = string.ascii_letters + string.digits + string.punctuation

os.system ('cls')

for quantity in range (quantity_of_passwords):

    secure_password = ''

    for password in range (size_of_password):

        secure_password += choice (characters)

    print (secure_password)

