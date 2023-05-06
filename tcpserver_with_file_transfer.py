
# coding: UTF-8

# tcpserver_with_file_transfer.py

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
    print ('\n* Copyright of Demétrio Freitas, 2023                                        *')
    print ('\n* https://github.com/DFSecurity                                              *')
    print ('\n* https://github.com/DFSecurity/Python/tcpserver_with_file_transfer.py       *')
    print ('\n******************************************************************************')
    print ('\n')

    os.system ('sleep 0.5')
    break

try:

    IP_or_host = input ('Type the IP or host: ')
    port = int (input ('Type the port: '))
    os.system ('clear')

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind ((IP_or_host, port))
    server.listen (1)

    print ('server: {} it is in listen in the port: {}'.format (IP_or_host, port))
    data, client = server.accept ()
    print ('client: {} is connected in the port: {}'.format (IP_or_host, port))

    result = data.recv (1024).decode ('UTF-8')

    with open ('transfer.txt', 'rb') as file:

        for lines in file.readlines ():

            data.send (lines)

        print ('\n')
        print ('Successfull at file transfer!')
        time.sleep (2.5)
        os.system ('clear')

except KeyboardInterrupt:

    subprocess.run (['clear'], shell=True)
    time.sleep (0.5)
    sys.exit ()

