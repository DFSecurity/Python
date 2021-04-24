
# coding: UTF-8

# portscan.py

import socket, os, sys

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/portscan.py                   *')
    print ('\n******************************************************************************')
    print ('\n')

    os.system ('sleep 0.5')
    
    Type_the_IP_or_Host_or_eE_to_exit = input ('Type the IP or Host or e / E to exit: ')
    os.system ('sleep 0.5')
    
    if Type_the_IP_or_Host_or_eE_to_exit == 'e' or Type_the_IP_or_Host_or_eE_to_exit == 'E':
        
        os.system ('clear')
        os.system ('sleep 0.5')
        break
        
    Type_the_Port = int (input ('Type the Port: '))
    os.system ('sleep 0.5')
    
    client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    code = client.connect_ex ((Type_the_IP_or_Host_or_eE_to_exit, Type_the_Port))
    os.system ('sleep 0.5')

    if code <= 0:

        os.system ('clear')
        os.system ('sleep 0.5')
        print (Type_the_Port, 'is open')
        os.system ('sleep 2.5')
        os.system ('clear')
        continue

    elif Type_the_Port >= 1:

        os.system ('clear')
        os.system ('sleep 0.5')
        print (Type_the_Port, 'is close')
        os.system ('sleep 2.5')
        os.system ('clear')
        continue
        
while True:
    
    os.system ('clear')
    os.system ('sleep 0.5')
    sys.exit ()
