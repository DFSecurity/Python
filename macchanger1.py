
# coding: UTF-8

# macchanger1.py

import subprocess, sys

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
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/macchanger1.py                *')
    print ('\n******************************************************************************')
    print ('\n')

    subprocess.run (['sleep 0.5'], shell=True)

    try:

        Type_the_interface_network_that_will_disable_or_eE_to_exit = input ('Type the interface network that will disable or e / E to exit: ')
        subprocess.run (['sleep 0.5'], shell=True)

        if Type_the_interface_network_that_will_disable_or_eE_to_exit == 'e' or Type_the_interface_network_that_will_disable_or_eE_to_exit == 'E':

            try:

                subprocess.run (['clear'], shell=True)
                subprocess.run (['sleep 0.5'], shell=True)
                break

            except:

                pass

        Type_the_new_MAC_Address_that_will_add = input ('Type the new MAC Address that will add: ')
        subprocess.run (['sleep 0.5'], shell=True)

        Type_the_interface_network_that_will_enable = input ('Type the interface network that will enable: ')
        subprocess.run (['sleep 0.5'], shell=True)

        subprocess.run ([f'ifconfig -a {Type_the_interface_network_that_will_disable_or_eE_to_exit} down'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        subprocess.run ([f'ifconfig -a {Type_the_interface_network_that_will_disable_or_eE_to_exit} hw ether {Type_the_new_MAC_Address_that_will_add}'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        subprocess.run ([f'ifconfig -a {Type_the_interface_network_that_will_enable} up'], shell=True)
        subprocess.run (['sleep 0.5'], shell=True)
        break

    except KeyboardInterrupt:

        break

while True:

    subprocess.run (['clear'], shell=True)
    subprocess.run (['sleep 0.5'], shell=True)
    sys.exit ()
