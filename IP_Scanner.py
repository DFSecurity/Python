
# coding: UTF-8

# IP_Scanner

import ipaddress, os

os.system ('cls')
user_profile = os.getlogin ()
IP_or_host = input ('IP or host with range: ')
generators = ipaddress.ip_network ('{}'.format (IP_or_host))
print ('\n')

if not os.path.exists (f'C:\\Users\\{user_profile}\\Desktop\\IPs.txt'):

    with open (f'C:\\Users\\{user_profile}\\Desktop\\IPs.txt', 'w') as file:

        for generator in generators:

            file.write ('{}\n'.format (generator))
            
    with open (f'C:\\Users\\{user_profile}\\Desktop\\IPs.txt', 'r') as file:

        IPs = file.readlines ()

        for IP in IPs:

            IP = IP.split () [0]
            response = os.popen (f'ping {IP} -n 1').read ()

            try:

                if 'Aproximar um n£mero redondo de vezes em milissegundos:' in response:
        
                    print ('\033[32m{} is up'.format (IP))

                elif 'Resposta de {}: Host de destino inacess¡vel.'.format (IP) or 'Esgotado o tempo limite do pedido.' in response:
        
                    print ('\033[31m{} is down'.format (IP))

            except:

            	pass
		    
elif os.path.exists (f'C:\\Users\\{user_profile}\\Desktop\\IPs.txt'):

    with open (f'C:\\Users\\{user_profile}\\Desktop\\IPs.txt', 'r') as file:

        IPs = file.readlines ()

        for IP in IPs:

            IP = IP.split () [0]
            response = os.popen (f'ping {IP} -n 1').read ()

            try:

                if 'Aproximar um n£mero redondo de vezes em milissegundos:' in response:
        
                    print ('\033[32m{} is up'.format (IP))

                elif 'Resposta de {}: Host de destino inacess¡vel.'.format (IP) or 'Esgotado o tempo limite do pedido.' in response:
        
                    print ('\033[31m{} is down'.format (IP))

            except:

            	pass

