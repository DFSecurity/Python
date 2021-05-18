
import socket

IP = input ('Type the IP or host or e / E to exit: ')

def connect (IP, port):

    try:

        client = socket.socket ()

        client.connect ((IP, port))

        client.settimeout (0.5)
        print (port, 'is open')

    except:

        pass

for port in range (21, 81):

    connect (IP, port)

