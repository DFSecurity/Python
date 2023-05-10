
# coding: UTF-8

# subdomains.py

import socket, os, time

os.system ('clear')

domain = input ('domain: ')

print ('\n')

if not os.path.exists ('subdomains.txt'):

    with open ('subdomains.txt', 'w') as file:

        file.write ('www\n')
        file.write ('ftp\n')
        file.write ('mail\n')
        file.write ('localhost\n')
        file.write ('webmail\n')
        file.write ('smtp\n')
        file.write ('support\n')
        file.write ('download\n')
        file.write ('files\n')
        file.write ('blog\n')

    time.sleep (2.5)

    with open ('subdomains.txt', 'r') as file:

        subdomains = file.readlines ()

    for subdomain in subdomains:

        result = subdomain.strip ('\n') + '.' + domain

        try:

            print (result + ': ' + socket.gethostbyname (result))

        except socket.gaierror:

            pass

    time.sleep (2.5)
    print ('\n')

elif os.path.exists ('subdomains.txt'):

    time.sleep (2.5)

    with open ('subdomains.txt', 'r') as file:

        subdomains = file.readlines ()

    for subdomain in subdomains:

        result = subdomain.strip ('\n') + '.' + domain

        try:

            print (result + ': ' + socket.gethostbyname (result))

        except socket.gaierror:

            pass

    time.sleep (2.5)
    print ('\n')
