
# coding: UTF-8

# SHA-1.py

import hashlib, subprocess, sys

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/SHA-1.py                      *')
    print ('\n******************************************************************************')
    print ('\n')

    Encrypt_or_eE_to_exit = input ('Encrypt or e / E to exit: ')

    subprocess.run (['sleep 0.5'], shell=True)
    subprocess.run (['clear'], shell=True)

    if Encrypt_or_eE_to_exit == 'e' or Encrypt_or_eE_to_exit == 'E':

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        break

    elif Encrypt_or_eE_to_exit:

        print ('SHA-1: {}:'.format (Encrypt_or_eE_to_exit), hashlib.sha1 (Encrypt_or_eE_to_exit.encode ('UTF-8')).hexdigest ())

        subprocess.run (['sleep 10'], shell=True)
        subprocess.run (['clear'], shell=True)
        continue

while True:

    subprocess.run (['clear'], shell=True)
    subprocess.run (['sleep 0.5'], shell=True)
    sys.exit ()

