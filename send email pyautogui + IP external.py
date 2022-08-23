
# coding: UTF-8

# send email pyautogui + IP external.py

import pyautogui
import requests
import subprocess
import time
import pyautogui as cursor
import sys
import os

while True:

    os.system ('cls')
    os.system ('timeout /t 1 > nul')

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/pyautogui.py                  *')
    print ('\n******************************************************************************')
    print ('\n')

    os.system ('timeout /t 10 > nul')
    os.system ('cls')
    break

while True:

    # collecting IP external

    subprocess.run (['cls'], shell=True)

    user_profile1 = os.getlogin ()

    IP_external = requests.get('https://api.ipify.org/').text
     
    with open (f'C:\\Users\\{user_profile1}\\Desktop\IP_external.txt', 'w', encoding='utf-8') as file1:

        file1.write (f"What's my IP: %s" % (IP_external))
        file1.close
        break  

while True:

    # reading file IP external.txt

    subprocess.run (['cls'], shell=True)
    os.system ('timeout /t 1 > nul')

    user_profile2 = os.getlogin ()
        
    with open (f'C:\\Users\\{user_profile1}\\Desktop\IP_external.txt', 'r', encoding='utf-8') as file2:

        results_finales = file2.read ()
        results_finales = results_finales.splitlines ()

        for result_final in results_finales:

            print ('%s' % (result_final))
                
            os.system ('timeout /t 10 > nul')
            subprocess.run (['cls'], shell=True)
        
        break

# pyautogui alert

pyautogui.alert ('The code will start... Do not use the computer while it is running!')
pyautogui.pause = 2.5

while True:

    # input EMAIL and PASSWORD

    Type_the_EMAIL1 = input ('Type the EMAIL: ')
    time.sleep (2.5)
    Type_the_PASSWORD = input ('Type_the_PASSWORD: ')
    os.system ('cls')

    # input EMAIL for destinatary

    Type_the_EMAIL2 = input ('Enter destination EMAIL: ')
    time.sleep (2.5)
    os.system ('cls')
    break

try:

    # opening the chrome

    cursor.moveTo (x=11, y=750)
    pyautogui.click ()
    pyautogui.press ('winleft')
    time.sleep (2.5)
    pyautogui.write ('chrome')
    time.sleep (2.5)
    pyautogui.press ('enter')
    time.sleep (2.5)

    # account login

    pyautogui.write ("https://accounts.google.com/signin")
    time.sleep (2.5)
    pyautogui.press ('enter')
    time.sleep (2.5)
    pyautogui.typewrite ('\n')
    time.sleep (2.5)
    pyautogui.write (Type_the_EMAIL1)
    time.sleep (2.5)
    pyautogui.press ('enter')
    time.sleep (2.5)
    pyautogui.write (Type_the_PASSWORD)
    time.sleep (2.5)
    pyautogui.press ('enter')
    time.sleep (2.5)

    # opening the gmail

    pyautogui.hotkey ('alt', 'home')
    time.sleep (2.5)
    pyautogui.write ("https://gmail.com/")
    time.sleep (2.5)
    pyautogui.press ('enter')

    # complementary time

    time.sleep (15.5)

    # write message to send

    cursor.moveTo (x=50, y=180)
    pyautogui.click ()
    time.sleep (5.5)
    pyautogui.typewrite ('\n')
    time.sleep (3.5)
    pyautogui.write (Type_the_EMAIL2)
    time.sleep (3.5)
    pyautogui.press ('enter')
    time.sleep (3.5)
    pyautogui.press ('tab')
    time.sleep (3.5)
    pyautogui.write ("What's my ip: %s" % (IP_external))
    time.sleep (3.5)
    pyautogui.press ('tab')
    time.sleep (3.5)
    pyautogui.hotkey ('ctrl', 'enter')
    time.sleep (3.5)
    pyautogui.hotkey ('ctrl', 't')
    time.sleep (3.5)
    pyautogui.write ('chrome://settings/clearBrowserData')
    time.sleep (3.5)
    pyautogui.press ('enter')
    time.sleep (3.5)
    cursor.moveTo (x=880, y=605)
    pyautogui.click ()
    time.sleep (3.5)
    subprocess.run (['cmd', '/k', 'powershell.exe', '-command', 'stop-process', '-name', 'chrome'], shell=True)
    time.sleep (3.5)
    os.system ('exit')
    time.sleep (3.5)
    os.remove (f'C:\\Users\\{user_profile1}\\Desktop\IP_external.txt')
    time.sleep (3.5)
    
    class finish:

        def message ():

            # finish and exit program pyautogui alert

            pyautogui.alert ('The code has been finalized... You can now use the computer !')
            pyautogui.pause = 2.5

        message ()

except:

    pass

    sys.exit ()
    exit ()

