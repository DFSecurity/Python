
import socket, threading, os

os.system ('cls')
clients = []
IP_or_host = input ('Type the IP or host: ')
Port = int (input ('Type the port: '))
os.system ('cls')

def main():

    client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

    try:
    
        client.connect ((IP_or_host, Port))
    
    except:
    
        return print ('\nError in conected in the server!\n')

    user = input ('User: ')
    print ('{} connected'.format (user))

    thread1 = threading.Thread (target = receive_messages, args = [client])
    thread2 = threading.Thread (target = send_messages, args = [client, user])

    thread1.start ()
    thread2.start ()


def receive_messages (client):

    while True:

        try:

            message = client.recv (4096).decode ('utf-8')
            print ('\n{}'.format (message))

        except:
        
            client.close ()
            break            

def send_messages (client, user):

    while True:
        
        try:
        
            print ('\n')
            message = input ('{}: '.format (user))
            client.send (f'{user}: {message}'.encode ('utf-8'))

        except:
            
            return

if __name__ == '__main__':

    main ()