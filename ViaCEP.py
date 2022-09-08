
# coding: UTF-8

# ViaCEP.py

import requests
import subprocess
import os
import time
import sys

def usage ():

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
    print ('\n* Copyright of Demétrio Freitas, 2022                                        *')
    print ('\n* https://github.com/PPrrooggrraammeerr                                      *')
    print ('\n* https://github.com/PPrrooggrraammeerr/Python/ViaCEP.py                     *')
    print ('\n******************************************************************************')
    print ('\n')

    print ('python3 ViaCEP.py -h')
    print ('\n')
    subprocess.run (['sleep 2.5'], shell=True)
    subprocess.run (['clear'], shell=True)
    sys.exit ()
    exit ()

def viacep (Type_the_CEP):

    time.sleep (0.5)
    os.system ('clear')

    try:

        cep = Type_the_CEP.replace ('-', '')

        if len (cep) == 8:

            link = f'https://viacep.com.br/ws/{cep}/json/'

            status = requests.get (link)

            dictionary = status.json ()

            cep = dictionary ['cep']
            logradouro = dictionary ['logradouro']
            bairro = dictionary ['bairro']
            localidade = dictionary ['localidade']
            uf = dictionary ['uf']
            ibge = dictionary ['ibge']
            gia = dictionary ['gia']
            ddd = dictionary ['ddd']
            siafi = dictionary ['siafi']

            print ('CEP: %s' % (cep))
            print ('Logradouro: %s' % (logradouro))
            print ('Bairro: %s' % (bairro))
            print ('Localidade: %s' % (localidade))
            print ('UF: %s' % (uf))
            print ('IBGE: %s' % (ibge))
            print ('GIA: %s' % (gia))
            print ('DDD: %s' % (ddd))
            print ('SIAFI: %s' % (siafi))

            time.sleep (2.5)
            os.system ('clear')

        else:

            print ('Invalid CEP')
            time.sleep (2.5)
            os.system ('clear')


    except:

        os.system ('clear')
        time.sleep (0.5)
        pass

    return Type_the_CEP

def main ():

    try:

        if sys.argv [1] == '-h':

            time.sleep (0.5)
            os.system ('clear')

            print ('python3 ViaCEP.py [CEP]')

            time.sleep (2.5)
            os.system ('clear')

        else:

            Type_the_CEP = (sys.argv [1])
            viacep (Type_the_CEP)

    except:

        usage ()

if __name__ == '__main__':

    main ()

while True:

    subprocess.run (['sleep 2.5'], shell=True)
    break

sys.exit ()
exit ()

