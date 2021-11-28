
# coding: UTF-8

# multiplerequests2.py

import requests, os, sys, time

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
    
    user_profile = os.getlogin ()
    
    requests_get = open (f'C:\\Users\\{user_profile}\\Desktop\requests.txt', 'w')

    requests = list ()
    
    requests.append ('https://solyd.com.br/\n')
    requests.append ('https://ftp.sunet.se/login/\n')
    requests.append ('https://google.com.br/404/\n')
    requests.append ('https://nube.com.br/CPF/\n')
    requests.append ('https://digitalinnovation.one/sign-in/\n')

    requests_get.writelines (requests)

    break

def main ():
    
    for request in requests:

        request = requests.get (request).status_code

        if request == 200:
        
            print ('status GET: {}'.format (request))

        elif request == 404:
    
            print ('status GET: {}'.format (request))

if __name__ == '__main__':

    main ()

time.sleep (2.5)
os.system ('cls')
sys.exit ()
exit ()

