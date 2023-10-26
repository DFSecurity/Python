
import socket, threading, os

os.system ('cls')
clients = []
IP_or_host = input ('Type the IP or host: ')
Port = int (input ('Type the port: '))
os.system ('cls')

def main ():

    server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

    try:
    
        server.bind ((IP_or_host, Port))
        server.listen ()
        
        print ('Server IP or host: {}'.format (IP_or_host))
        print ('Open port: {}'.format (Port))
        print ('\n')
    
    except:
    
        return print('\nError in the server!')

    while True:
    
        client, addr = server.accept ()
        clients.append (client)
        
        thread = threading.Thread (target = messages_treatments, args = [client])
        thread.start ()

def messages_treatments (client):

    while True:
 
        try:
       
            message = client.recv (2048)
            broadcast (message, client)
     
        except:
   
            remove_client (client)
            break

def broadcast (message, client):

    for customer in clients:

        if customer != client:

            try:

                customer.send (message)

            except:

                remove_client (customer)

def remove_client (client):

    clients.remove (client)

main ()