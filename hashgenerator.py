
# coding: UTF-8

# hashgenerator.py

import hashlib, subprocess, sys, os, time

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/hashgenerator.py              *')
    print ('\n******************************************************************************')
    print ('\n')

    try:

        Encrypt_or_eE_to_exit = input ('Encrypt or e / E to exit: ')

        subprocess.run (['sleep 0.5'], shell=True)
        subprocess.run (['clear'], shell=True)

        if Encrypt_or_eE_to_exit == 'e' or Encrypt_or_eE_to_exit == 'E':

            subprocess.run (['clear'], shell=True)
            subprocess.run (['sleep 0.5'], shell=True)
            break

        elif Encrypt_or_eE_to_exit:

            print ('\n')
            print ('\n*******************')
            print ('\n* 1 - MD5         *')
            print ('\n* 2 - SHA-1       *')
            print ('\n* 3 - SHA-256     *')
            print ('\n* 4 - SHA-512     *')
            print ('\n*******************')
            print ('\n')

            subprocess.run (['sleep 0.5'], shell=True)
            Type_the_option = int (input ('Type the option: '))
            subprocess.run (['sleep 0.5'], shell=True)
            subprocess.run (['clear'], shell=True)

            if Type_the_option == 1:

                print ('MD5: {}:'.format (Encrypt_or_eE_to_exit), hashlib.md5 (Encrypt_or_eE_to_exit.encode ('UTF-8')).hexdigest ())

                subprocess.run (['sleep 10'], shell=True)
                subprocess.run (['clear'], shell=True)
                continue

            elif Type_the_option == 2:

                print ('SHA-1: {}:'.format (Encrypt_or_eE_to_exit), hashlib.sha1 (Encrypt_or_eE_to_exit.encode ('UTF-8')).hexdigest ())

                subprocess.run (['sleep 10'], shell=True)
                subprocess.run (['clear'], shell=True)
                continue

            elif Type_the_option == 3:

                print ('SHA-256: {}:'.format (Encrypt_or_eE_to_exit), hashlib.sha256 (Encrypt_or_eE_to_exit.encode ('UTF-8')).hexdigest ())

                subprocess.run (['sleep 10'], shell=True)
                subprocess.run (['clear'], shell=True)
                continue

            elif Type_the_option == 4:

                print ('SHA-512: {}:'.format (Encrypt_or_eE_to_exit), hashlib.sha512 (Encrypt_or_eE_to_exit.encode ('UTF-8')).hexdigest ())

                subprocess.run (['sleep 10'], shell=True)
                subprocess.run (['clear'], shell=True)
                continue

    except KeyboardInterrupt:

        subprocess.run (['clear'], shell=True)
        time.sleep (0.5)
        sys.exit ()

while True:

    os.system ('clear')
    time.sleep (0.5)
    sys.exit ()

