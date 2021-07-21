
# pingmultiplewebsites1.py

# coding: UTF-8

import os, sys, time

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/pingmultiplewebsites1.py      *')
    print ('\n******************************************************************************')
    print ('\n')

    os.system ('timeout /t 10 > nul')
    os.system ('cls')

    with open ('C:\\Users\Helena\Websites.txt', 'w') as arq1:

        arq1.write ('192.168.0.1\n')
        arq1.write ('www.google.com\n')
        arq1.write ('www.youtube.com\n')
        arq1.write ('www.facebook.com\n')
        arq1.write ('github.com\n')
        arq1.write ('ftp.sunet.se\n')
        arq1.write ('pt.wikipedia.org\n')
        arq1.write ('194.71.11.173\n')
        
        break

with open ('C:\\Users\Helena\Websites.txt') as arq2:
    
    websites = arq2.read ()
    websites = websites.splitlines ()
    
    for website in websites:
    
        try:
            
            os.system ('timeout /t 0 > nul')
            os.system ('ping {}'.format (website))

            time.sleep (0.5)
                
        except KeyboardInterrupt:
            
            os.system ('cls')
            time.sleep (0.5)
            sys.exit ()

