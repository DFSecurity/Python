
# p_ou_i

import os, time

os.system ('clear')
time.sleep (1)
Type_the_number = int (input ('Type the number: '))

class p_ou_i:

    def __init__ (self, number):

        self.number = Type_the_number

    def definition (self):

        return self.number

definition_and_result = p_ou_i (Type_the_number)

if definition_and_result.definition () % 2 == 0:

    os.system ('clear')
    print ('número par')
    time.sleep (1)
    os.system ('clear')

else:

    os.system ('clear')
    print ('número ímpar')
    time.sleep (1)
    os.system ('clear')

exit ()

