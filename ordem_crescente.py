
# coding: UTF-8

# ordem_crescente.py

import os, time

os.system ('clear')

value1 = int (input ('value1: '))
value2 = int (input ('value2: '))
value3 = int (input ('value3: '))

if value1 < value2:

    if value2 < value3:

        os.system ('clear')
        print (value1, value2, value3)
        time.sleep (2.5)
        os.system ('clear')

    else:

        if value1 > value3:

            os.system ('clear')
            print (value3, value1, value2)
            time.sleep (2.5)
            os.system ('clear')

        else:

            os.system ('clear')
            print (value1, value3, value2)
            time.sleep (2.5)
            os.system ('clear')

else:

    if value2 > value3:

        os.system ('clear')
        print (value3, value2, value1)
        time.sleep (2.5)
        os.system ('clear')

    else:

        if value3 > value2:

            os.system ('clear')
            print (value2, value3, value1)
            time.sleep (2.5)
            os.system ('clear')

        else:

            os.system ('clear')
            print (value2, value3, value1)
            time.sleep (2.5)
            os.system ('clear')

exit ()

