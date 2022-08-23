
# coding: UTF-8

# calculator1.py

import subprocess, sys

while True:

    subprocess.run (['clear'], shell=True)
    subprocess.run (['sleep 0.5'], shell=True)

    print ('\n')
    print ('******************************************************************************')
    print (r"""
                         _
 ____                   /_/_        _         _____         _ _              *  
|  _ \  ___ _ __ ___   ___| |_ _ __(_) ___   |  ___| __ ___(_) |_ __ _ ___
| | | |/ _ \ '_ ` _ \ / _ \ __| '__| |/ _ \  | |_ | '__/ _ \ | __/ _` / __|  *
| |_| |  __/ | | | | |  __/ |_| |  | | (_) | |  _|| | |  __/ | || (_| \__ \
|____/ \___|_| |_| |_|\___|\__|_|  |_|\___/  |_|  |_|  \___|_|\__\__,_|___/  *

    """)
    
    print ('\n******************************************************************************')
    print ('\n* Copyright of Demétrio Freitas, 2021                                        *')
    print ('\n* https://github.com/PPrrooggrraammeerr                                      *')
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/calculator1.py                *')
    print ('\n******************************************************************************')
    print ('\n')

    subprocess.run (['sleep 0.5'], shell=True)
    
    Type_the_operation = input ('Type the operation (+, -, *, /) you want to perform or e/E to exit: ')
    subprocess.run (['sleep 0.5'], shell=True)

    if Type_the_operation == 'e' or Type_the_operation == 'E':

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        break

    elif Type_the_operation == '+' or Type_the_operation == '-' or Type_the_operation == '*' or Type_the_operation == '/':

        subprocess.run (['clear'], shell=True)
        Type_the_first_number = int (input ('Type the first number: '))
        subprocess.run (['sleep 0.5'], shell=True)
        
        subprocess.run (['clear'], shell=True)
        Type_the_second_number = int (input ('Type the second number: '))
        subprocess.run (['sleep 0.5'], shell=True)

    else:

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        print ('Wrong operation')
        subprocess.run (['sleep 2.5'], shell=True)
        subprocess.run (['clear'], shell=True)
        break

    if Type_the_operation == '+':

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        result = (Type_the_first_number + Type_the_second_number)
        print (result)
        subprocess.run (['sleep 2.5'], shell=True)
        subprocess.run (['clear'], shell=True)
        continue
        
    elif Type_the_operation == '-':

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        result = (Type_the_first_number - Type_the_second_number)
        print (result)
        subprocess.run (['sleep 2.5'], shell=True)
        subprocess.run (['clear'], shell=True)
        continue

    elif Type_the_operation == '*':

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        result = (Type_the_first_number * Type_the_second_number)
        print (result)
        subprocess.run (['sleep 2.5'], shell=True)
        subprocess.run (['clear'], shell=True)
        continue

    elif Type_the_operation == '/':

        try:
        
            subprocess.run (['clear'], shell=True)
            subprocess.run (['sleep 0.5'], shell=True)
            result = (Type_the_first_number / Type_the_second_number)
            print (result)
            subprocess.run (['sleep 2.5'], shell=True)
            subprocess.run (['clear'], shell=True)
            continue

        except ZeroDivisionError:
        
            pass
        
while True:

    subprocess.run (['clear'], shell=True)
    subprocess.run (['sleep 0.5'], shell=True)
    sys.exit ()
