
# coding: UTF-8

# IPaddressoptions.py

import socket, requests, subprocess, sys, os, time

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/IPaddressoptions.py           *')
    print ('\n******************************************************************************')
    print ('\n')

    subprocess.run (['sleep 2.5'], shell=True)
    subprocess.run (['clear'], shell=True)
    break

while True:

    def main ():

        try:

            print ('\n')
            print ('\n***********************')
            print ('\n*  1 - IP internal    *')
            print ('\n*  2 - IP external    *')
            print ('\n*  3 - IP localhost   *')
            print ('\n*  4 - Exit program   *')
            print ('\n***********************')
            print ('\n')

            subprocess.run (['sleep 0.5'], shell=True)
            Type_the_option = int (input ("What's my IP? Type the option: "))

            if Type_the_option == 1:

                subprocess.run (['clear'], shell=True)

                client = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
                client.connect (('8.8.8.8', 80))
                result = client.getsockname () [0]

                print ("What's my IP internal: {}".format (result))
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_option == 2:

                subprocess.run (['clear'], shell=True)

                IP_external = requests.get('https://api.ipify.org/').text

                print (f"What's my IP external: {IP_external}")
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_option == 3:

                subprocess.run (['clear'], shell=True)

                hostname = socket.gethostname()
                localhost = socket.gethostbyname(hostname)

                print ("What's my IP localhost: {}".format (localhost))
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_option == 4:

                os.system ('clear')
                time.sleep (0.5)
                sys.exit ()
                exit ()

        except KeyboardInterrupt:

            subprocess.run (['clear'], shell=True)
            time.sleep (0.5)
            sys.exit ()
            exit ()

    if __name__ == '__main__':

        main ()

while True:

    os.system ('clear')
    time.sleep (0.5)
    sys.exit ()
    exit ()

