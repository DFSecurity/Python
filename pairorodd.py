
# coding: UTF-8

# pairorodd.py

import subprocess, os, sys, time

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/pairorodd.py                  *')
    print ('\n******************************************************************************')
    print ('\n')

    subprocess.run (['sleep 0.5'], shell=True)
    subprocess.run (['clear'], shell=True)

    def pair_or_odd ():

        try:

            Type_the_number = int (input ('Type the number: '))
            subprocess.run (['sleep 0.5'], shell=True)
            subprocess.run (['clear'], shell=True)

        except KeyboardInterrupt:

            subprocess.run (['clear'], shell=True)
            time.sleep (0.5)
            sys.exit ()

        if (Type_the_number % 2) == 0:

            try:

                print (f'Number %s is pair' % (Type_the_number))
                subprocess.run (['sleep 0.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            except KeyboardInterrupt:

                subprocess.run (['clear'], shell=True)
                time.sleep (0.5)
                sys.exit ()

        elif (Type_the_number % 2) >= 1:

            try:

                print (f'Number %s is odd' % (Type_the_number))
                subprocess.run (['sleep 0.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            except KeyboardInterrupt:

                subprocess.run (['clear'], shell=True)
                time.sleep (0.5)
                sys.exit ()

    pair_or_odd ()

    break

while True:

    os.system ('clear')
    time.sleep (0.5)
    sys.exit ()
