
# coding: UTF-8

# tcpconnection.py

import socket, subprocess, sys

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/tcpconnection.py              *')
    print ('\n******************************************************************************')
    print ('\n')

    subprocess.run (['sleep 0.5'], shell=True)

    Type_the_IP_or_Host_or_eE_to_exit = input ('Type the IP or Host or e / E to exit: ')
    subprocess.run (['sleep 0.5'], shell=True)

    if Type_the_IP_or_Host_or_eE_to_exit == 'e' or Type_the_IP_or_Host_or_eE_to_exit == 'E':

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        break

    Type_the_port = int (input ('Type the port: '))
    subprocess.run (['sleep 0.5'], shell=True)

    tcpconnection = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    code = tcpconnection.connect_ex ((Type_the_IP_or_Host_or_eE_to_exit, Type_the_port))
    subprocess.run (['sleep 0.5'], shell=True)

    if code <= 0:

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        print ('TCP/IP: connected')
        tcpconnection.shutdown (1)
        tcpconnection.close ()

        subprocess.run (['sleep 2.5'], shell=True)
        subprocess.run (['clear'], shell=True)
        continue

    elif code >= 1:

        subprocess.run (['clear'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        print ('TCP/IP: not connected')
        tcpconnection.close ()

        subprocess.run (['sleep 2.5'], shell=True)
        subprocess.run (['clear'], shell=True)
        continue

while True:

    subprocess.run (['clear'], shell=True)
    subprocess.run (['sleep 0.5'], shell=True)
    sys.exit ()

