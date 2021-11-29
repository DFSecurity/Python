
# coding: UTF-8

# multiplerequests2.py

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/multiplerequests2.py          *')
    print ('\n******************************************************************************')
    print ('\n')

    os.system ('timeout /t 10 > nul')
    os.system ('cls')
    
    user_profile1 = os.getlogin ()
    
    with open (f'C:\\Users\\{user_profile1}\\Desktop\Websites.txt', 'w') as websites1:
    
        websites1.write ('https://solyd.com.br/\n')
        websites1.write ('https://ftp.sunet.se/login/\n')
        websites1.write ('https://google.com.br/404/\n')
        websites1.write ('https://nube.com.br/CPF/\n')
        websites1.write ('https://digitalinnovation.one/sign-in/\n')

        break

def main ():

    user_profile2 = os.getlogin ()

    with open (f'C:\\Users\\{user_profile2}\\Desktop\Websites.txt') as websites2:

        websites = websites2.read ()
        websites = websites.splitlines ()
    
        for website in websites:

            requests_get = requests.get (website).status_code

            if requests_get == 200:
                
                print ('status GET: {}'.format (requests_get))
                    
            elif requests_get == 404:

                print ('status GET: {}'.format (requests_get))

if __name__ == '__main__':

    main ()

while True:

    time.sleep (2.5)
    subprocess.run (['cls'], shell=True)
    sys.exit ()
    exit ()

