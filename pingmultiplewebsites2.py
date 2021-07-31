
# pingmultiplewebsites2.py

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/pingmultiplewebsites2.py      *')
    print ('\n******************************************************************************')
    print ('\n')

    os.system ('timeout /t 10 > nul')
    os.system ('cls')

    user_profile = os.getlogin ()
    
    arq1 = open (f'C:\\Users\\{user_profile}\\Desktop\Websites2.txt', 'w')

    arqs = list ()
    
    arqs.append ('192.168.0.1\n')
    arqs.append ('www.google.com\n')
    arqs.append ('www.youtube.com\n')
    arqs.append ('www.facebook.com\n')
    arqs.append ('github.com\n')
    arqs.append ('ftp.sunet.se\n')
    arqs.append ('pt.wikipedia.org\n')
    arqs.append ('194.71.11.173\n')

    arq1.writelines (arqs)
    
    break
    
for arq in arqs:
    
    try:
        
        os.system ('timeout /t 0 > nul')
        os.system ('ping {}'.format (arq))
        
        time.sleep (0.5)

    except KeyboardInterrupt:
        
        os.system ('cls')
        time.sleep (0.5)
        sys.exit ()

