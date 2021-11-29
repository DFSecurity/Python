
# coding: UTF-8

# multiplerequests1.py

import requests, os, sys, time, subprocess

while True:

    os.system ('cls')
    os.system ('timeout /t 0 > nul')

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/multiplerequests1.py          *')
    print ('\n******************************************************************************')
    print ('\n')

    os.system ('timeout /t 10 > nul')
    os.system ('cls')
    
    requests_get = [
    
    'https://solyd.com.br/',
    'https://ftp.sunet.se/login/',
    'https://google.com.br/404/',
    'https://nube.com.br/CPF/',
    'https://digitalinnovation.one/sign-in/',

     ]

    break

def main ():
    
    for request_get in requests_get:

        request_get = requests.get (request_get).status_code

        if request_get == 200:
        
            print ('status GET: {}'.format (request_get))

        elif request_get == 404:
    
            print ('status GET: {}'.format (request_get))

if __name__ == '__main__':

    main ()

while True:

    time.sleep (2.5)
    subprocess.run (['cls'], shell=True)
    sys.exit ()
    exit ()
