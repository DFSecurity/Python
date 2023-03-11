
# coding: UTF-8

# idealparaoexercito.py

import os, time

class exercito:

    os.system ('clear')

    idade = int (input ('Informe sua idade: '))
    altura = float (input ('Informe sua altura: '))
    peso = int (input ('Informe seu peso: '))

    os.system ('clear')

    def main (self, idade, altura, peso):

        self.idade = idade
        self.altura = altura
        self.peso = peso

    def resultado (self):

        if self.idade >= 18 and self.altura >= 1.70 and self.peso >= 60:

            try:

                print ('Parabéns! Você possui todos os requisitos mínimos para servir ao exército, veja: ')
                time.sleep (2.5)
                print ('\n')
                print ('\033[32m'+'Idade: %s anos de idade;' % (self.idade))
                print ('\033[32m'+'Altura: %s de altura;' % (self.altura))
                print ('\033[32m'+'Peso: %s quilos.' % (self.peso))
                time.sleep (4.5)
                os.system ('clear')

            except KeyboardInterrupt:

                os.system ('clear')
                pass

        elif self.idade < 18 and self.altura >= 1.70 and self.peso >= 60:

            try:

                print ('Infelizmente você não possui todos os requisitos mínimos para servir ao exército, veja: ')
                time.sleep (2.5)
                print ('\n')
                print ('\033[31m'+'Idade: %s anos de idade;' % (self.idade))
                print ('\033[32m'+'Altura: %s de altura;' % (self.altura))
                print ('\033[32m'+'Peso: %s quilos.' % (self.peso))
                time.sleep (4.5)
                os.system ('clear')

            except KeyboardInterrupt:

                os.system ('clear')
                pass

        elif self.idade >= 18 and self.altura < 1.70 and self.peso >= 60:

            try:

                print ('Infelizmente você não possui todos os requisitos mínimos para servir ao exército, veja: ')
                time.sleep (2.5)
                print ('\n')
                print ('\033[32m'+'Idade: %s anos de idade;' % (self.idade))
                print ('\033[31m'+'Altura: %s de altura;' % (self.altura))
                print ('\033[32m'+'Peso: %s quilos.' % (self.peso))
                time.sleep (4.5)
                os.system ('clear')

            except KeyboardInterrupt:

                os.system ('clear')
                pass

        elif self.idade >= 18 and self.altura >= 1.70 and self.peso < 60:

            try:

                print ('Infelizmente você não possui todos os requisitos mínimos para servir ao exército, veja: ')
                time.sleep (2.5)
                print ('\n')
                print ('\033[32m'+'Idade: %s anos de idade;' % (self.idade))
                print ('\033[32m'+'Altura: %s de altura;' % (self.altura))
                print ('\033[31m'+'Peso: %s quilos.' % (self.peso))
                time.sleep (4.5)
                os.system ('clear')

            except KeyboardInterrupt:

                os.system ('clear')
                pass

        elif self.idade < 18 and self.altura < 1.70 and self.peso >= 60:

            try:

                print ('Infelizmente você possui apenas um requisito mínimo para servir ao exército, veja: ')
                time.sleep (2.5)
                print ('\n')
                print ('\033[31m'+'Idade: %s anos de idade;' % (self.idade))
                print ('\033[31m'+'Altura: %s de altura;' % (self.altura))
                print ('\033[32m'+'Peso: %s quilos.' % (self.peso))
                time.sleep (4.5)
                os.system ('clear')

            except KeyboardInterrupt:

                os.system ('clear')
                pass

        elif self.idade >= 18 and self.altura < 1.70 and self.peso < 60:

            try:

                print ('Infelizmente você possui apenas um requisito mínimo para servir ao exército, veja: ')
                time.sleep (2.5)
                print ('\n')
                print ('\033[32m'+'Idade: %s anos de idade;' % (self.idade))
                print ('\033[31m'+'Altura: %s de altura;' % (self.altura))
                print ('\033[31m'+'Peso: %s quilos.' % (self.peso))
                time.sleep (4.5)
                os.system ('clear')

            except KeyboardInterrupt:

                os.system ('clear')
                pass

        elif self.idade < 18 and self.altura >= 1.70 and self.peso < 60:

            try:

                print ('Infelizmente você possui apenas um requisito mínimo para servir ao exército, veja: ')
                time.sleep (2.5)
                print ('\n')
                print ('\033[31m'+'Idade: %s anos de idade;' % (self.idade))
                print ('\033[32m'+'Altura: %s de altura;' % (self.altura))
                print ('\033[31m'+'Peso: %s quilos.' % (self.peso))
                time.sleep (4.5)
                os.system ('clear')

            except KeyboardInterrupt:

                os.system ('clear')
                pass

        elif self.idade < 18 and self.altura < 1.70 and self.peso < 60:

            try:

                print ('Infelizmente você não possui os requisitos mínimo para servir ao exército, veja: ')
                time.sleep (2.5)
                print ('\n')
                print ('\033[31m'+'Idade: %s anos de idade;' % (self.idade))
                print ('\033[31m'+'Altura: %s de altura;' % (self.altura))
                print ('\033[31m'+'Peso: %s quilos.' % (self.peso))
                time.sleep (4.5)
                os.system ('clear')

            except KeyboardInterrupt:

                os.system ('clear')
                pass

call = exercito ()

call.resultado ()

