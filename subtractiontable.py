
# coding: UTF-8

# subtractiontable.py

import subprocess

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
    print ('\n* Copyright of Demétrio Freitas, 2022                                        *')
    print ('\n* https://github.com/PPrrooggrraammeerr                                      *')
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/subtractiontable.py           *')
    print ('\n******************************************************************************')
    print ('\n')

    subprocess.run (['sleep 2.5'], shell=True)
    subprocess.run (['clear'], shell=True)
    break

while True:

    one = 1

    numbers = range (1, 11)

    print ('\n')
    print ('Tabuada de Subtração')
    print ('\n')

    print ('Tabuada do {}'.format (one))
    print ('\n')

    print ('============')

    for number in numbers:

        print (one + number, '-', one, '=', number)

    print ('============')
    print ('\n')

    print ('Tabuada do {}'.format (one + one))
    print ('\n')

    print ('============')

    for number in numbers:

        print (number + one + one, '-', one + one, '=', number)

    print ('============')
    print ('\n')

    print ('Tabuada do {}'.format (one + one + one))
    print ('\n')

    print ('============')

    for number in numbers:

        print (number + one + one + one, '-', one + one + one, '=', number)

    print ('============')
    print ('\n')

    print ('Tabuada do {}'.format (one + one + one + one))
    print ('\n')

    print ('============')

    for number in numbers:

        print (number + one + one + one + one, '-', one + one + one + one, '=', number)

    print ('============')
    print ('\n')

    print ('Tabuada do {}'.format (one + one + one + one + one))
    print ('\n')

    print ('============')

    for number in numbers:

        print (number + one + one + one + one + one, '-', one + one + one + one + one, '=', number)

    print ('============')
    print ('\n')

    print ('Tabuada do {}'.format (one + one + one + one + one + one))
    print ('\n')

    print ('============')

    for number in numbers:

        print (number + one + one + one + one + one + one, '-', one + one + one + one + one + one, '=', number)

    print ('============')
    print ('\n')

    print ('Tabuada do {}'.format (one + one + one + one + one + one + one))
    print ('\n')

    print ('============')

    for number in numbers:

        print (number + one + one + one + one + one + one + one, '-', one + one + one + one + one + one + one, '=', number)

    print ('============')
    print ('\n')

    print ('Tabuada do {}'.format (one + one + one + one + one + one + one + one))
    print ('\n')

    print ('============')

    for number in numbers:

        print (number + one + one + one + one + one + one + one + one, '-', one + one + one + one + one + one + one + one, '=', number)

    print ('============')
    print ('\n')

    print ('Tabuada do {}'.format (one + one + one + one + one + one + one + one + one))
    print ('\n')

    print ('============')

    for number in numbers:

        print (number + one + one + one + one + one + one + one + one + one, '-', one + one + one + one + one + one + one + one + one, '=', number)

    print ('============')
    print ('\n')

    print ('Tabuada do {}'.format (one + one + one + one + one + one + one + one + one + one))
    print ('\n')

    print ('============')

    for number in numbers:

        print (number + one + one + one + one + one + one + one + one + one + one, '-', one + one + one + one + one + one + one + one + one + one, '=', number)

    print ('============')
    print ('\n')
    break

def finish ():

    exit ()

finish ()
