
# coding: UTF-8

# ping_in_multiple_IPs_and_hosts_with_results.py

import os, time

os.system ('cls')

user_profile = os.getlogin ()

if not os.path.exists (f'C:\\Users\\{user_profile}\\Desktop\IPs_and_hosts.txt'):

    with open (f'C:\\Users\\{user_profile}\\Desktop\IPs_and_hosts.txt', 'w') as file:

        file.write ('192.168.0.1\n')
        file.write ('192.168.0.10\n')
        file.write ('192.168.0.11\n')
        file.write ('192.168.0.12\n')
        file.write ('192.168.0.13\n')
        file.write ('192.168.0.14\n')
        file.write ('192.168.0.15\n')
        file.write ('192.168.0.16\n')
        file.write ('192.168.0.17\n')
        file.write ('192.168.0.18\n')
        file.write ('192.168.0.19\n')
        file.write ('192.168.0.20\n')
        
    time.sleep (2.5)
        
    with open (f'C:\\Users\\{user_profile}\\Desktop\IPs_and_hosts.txt', 'r') as file:

        IPs_and_hosts = file.read ()
        IPs_and_hosts = IPs_and_hosts.splitlines ()
        
    for IP_and_host in IPs_and_hosts:
    
        IP_and_host = IP_and_host.split () [0]
        response = os.popen (f'ping {IP_and_host} -n 1').read ()
        
        if 'Aproximar um n£mero redondo de vezes em milissegundos:' in response:
        
            print ('{} is up'.format (IP_and_host))
            
        elif 'Resposta de {}: Host de destino inacess¡vel.'.format (IP_and_host) or 'Esgotado o tempo limite do pedido.' in response:
        
            print ('{} is down'.format (IP_and_host))
        
    os.remove (f'C:\\Users\\{user_profile}\\Desktop\IPs_and_hosts.txt')

elif os.path.exists (f'C:\\Users\\{user_profile}\\Desktop\IPs_and_hosts.txt'):

    time.sleep (2.5)

    with open (f'C:\\Users\\{user_profile}\\Desktop\IPs_and_hosts.txt', 'r') as file:

        IPs_and_hosts = file.read ()
        IPs_and_hosts = IPs_and_hosts.splitlines ()
        
    for IP_and_host in IPs_and_hosts:
    
        IP_and_host = IP_and_host.split () [0]
        response = os.popen (f'ping {IP_and_host} -n 1').read ()
        
        if 'Aproximar um n£mero redondo de vezes em milissegundos:' in response:
        
            print ('{} is up'.format (IP_and_host))
            
        elif 'Resposta de {}: Host de destino inacess¡vel.'.format (IP_and_host) or 'Esgotado o tempo limite do pedido.' in response:
        
            print ('{} is down'.format (IP_and_host))

    os.remove (f'C:\\Users\\{user_profile}\\Desktop\IPs_and_hosts.txt')

time.sleep (2.5)
os.system ('cls')
