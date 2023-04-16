
# coding: UTF-8

# tables_with_basic_mathematical_operations.py

import subprocess, os

while True:

    subprocess.run (['clear'], shell=True)
    subprocess.run (['sleep 0.5'], shell=True)

    operation = input ('Type the operation (+, -, *, /) you want to perform or e/E to exit: ')
    subprocess.run (['sleep 0.5'], shell=True)
    subprocess.run (['clear'], shell=True)
    value = int (input ('Type the number of table: '))
    subprocess.run (['sleep 0.5'], shell=True)

    if operation == 'e' or operation == 'E':

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        break

    elif operation == '+' or operation == '-' or operation == '*' or operation == '/':

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)

    else:

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        print ('Wrong operation')
        subprocess.run (['sleep 2.5'], shell=True)
        subprocess.run (['clear'], shell=True)
        break

    if operation == '+':

        print ('\n')

        for number in range (10+1):

            print (f'%d %s %d = %d' % (value, operation, number, value + number))

        break

    elif operation == '-':

        print ('\n')

        for number in range (10+1):

            print (f'%d %s %d = %d' % (number+value, operation, value, number + value - value))

        break

    elif operation == '*':

        print ('\n')

        for number in range (10+1):

            print (f'%d %s %d = %d' % (value, operation, number, value * number))

        break

    else:

        print ('\n')

        for number in range (1, 10+1):

            print (f'%d %s %d = %d' % (number*value, operation, value, number * value / value))

        break

print ('\n')

subprocess.run (['sleep 2.5'], shell=True)
subprocess.run (['clear'], shell=True)

