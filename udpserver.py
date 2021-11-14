
# coding: UTF-8

# udpserver.py

import socket, subprocess, time, sys, os

while True:

    os.system ('clear')
    os.system ('sleep 0.5')

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/udpserver.py                  *')
    print ('\n******************************************************************************')
    print ('\n')

    os.system ('sleep 0.5')
    break

while True:

    try:

        server = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

        Type_the_IP_or_host = input ('Type the IP or host: ')
        Type_the_port = int (input ('Type the port: '))

        time.sleep (0.5)
        subprocess.run (['clear'], shell=True)

        server.bind ((Type_the_IP_or_host, Type_the_port))

        print ('server IP or host: {}'.format (Type_the_IP_or_host))
        print ('open port: {}'.format (Type_the_port))
        print ('\n')
        break

    except KeyboardInterrupt:

        subprocess.run (['clear'], shell=True)
        time.sleep (0.5)
        sys.exit ()

while True:

    try:

        dice, client = server.recvfrom (1024)
        dice = (dice.decode ('UTF-8'))
        print ('client: {}'.format (dice))

        message = input ('server: ')

        server.sendto (message.encode ('UTF-8'), (client))

    except KeyboardInterrupt:

        subprocess.run (['clear'], shell=True)
        time.sleep (0.5)
        sys.exit ()
