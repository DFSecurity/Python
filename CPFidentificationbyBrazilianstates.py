
import sys, subprocess, os, time

def usage ():

    print ('python3 CPFidentificationbyBrazilianstates.py -h')
    subprocess.run (['sleep 2.5'], shell=True)
    subprocess.run (['clear'], shell=True)
    sys.exit ()
    exit ()

def function (Type_the_state_or_acronym):

    time.sleep (0.5)
    os.system ('clear')

    estados_brasileiros = ['Acre', 'AC', 'Alagoas', 'AL', 'Amapá', 'AP', 'Amazonas', 'AM', 'BahCia', 'BA', 'Ceará', 'CE', 'Distrito Federal', 'DF', 'Espírito Santo', 'ES', 'Goiás', 'GO', 'Maranhão', 'MA', 'Mato Grosso', 'MT', 'Mato Grosso do Sul', 'MS', 'Minas Gerais', 'MG', 'Pará', 'PA', 'Paraíba', 'PB', 'Paraná', 'PR', 'Pernambuco', 'PE', 'Piauí', 'PI', 'Rio de Janeiro', 'RJ', 'Rio Grande do Norte', 'RN', 'Rio Grande do Sul', 'RS', 'Rondônia', 'RO', 'Roraima', 'RR', 'Santa Catarina', 'SC', 'São Paulo', 'SP', 'Sergipe', 'SE', 'Tocantins', 'TO']

    try:

        if Type_the_state_or_acronym in estados_brasileiros:

            if Type_the_state_or_acronym == 'Rio Grande do Sul' or Type_the_state_or_acronym == 'RS':

                print ('Brazilian state or acronym: %s' % (Type_the_state_or_acronym))
                print ('CPF identification: 111.111.110-11')
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_state_or_acronym == 'Distrito Federal' or Type_the_state_or_acronym == 'DF' or Type_the_state_or_acronym == 'Goiás' or Type_the_state_or_acronym == 'GO' or Type_the_state_or_acronym == 'Mato Grosso' or Type_the_state_or_acronym == 'MT' or Type_the_state_or_acronym == 'Mato Grosso do Sul' or Type_the_state_or_acronym == 'MS' or Type_the_state_or_acronym == 'Tocantins' or Type_the_state_or_acronym == 'TO':

                print ('Brazilian state or acronym: %s' % (Type_the_state_or_acronym))
                print ('CPF identification: 222.222.221-22')
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_state_or_acronym == 'Amazonas' or Type_the_state_or_acronym == 'AM' or Type_the_state_or_acronym == 'Pará' or Type_the_state_or_acronym == 'PA' or Type_the_state_or_acronym == 'Roraima' or Type_the_state_or_acronym == 'RO' or Type_the_state_or_acronym == 'Amapá' or Type_the_state_or_acronym == 'AP' or Type_the_state_or_acronym == 'Acre' or Type_the_state_or_acronym == 'AC' or Type_the_state_or_acronym == 'Rondônia' or Type_the_state_or_acronym == 'RO':

                print ('Brazilian state or acronym: %s' % (Type_the_state_or_acronym))
                print ('CPF identification: 333.333.332-33')
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_state_or_acronym == 'Ceará' or Type_the_state_or_acronym == 'CE' or Type_the_state_or_acronym == 'Maranhão' or Type_the_state_or_acronym == 'MA' or Type_the_state_or_acronym == 'Piauí' or Type_the_state_or_acronym == 'PI':

                print ('Brazilian state or acronym: %s' % (Type_the_state_or_acronym))
                print ('CPF identification: 444.444.443-44')
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_state_or_acronym == 'Paraíba' or Type_the_state_or_acronym == 'PB' or Type_the_state_or_acronym == 'Pernambuco' or Type_the_state_or_acronym == 'PE' or Type_the_state_or_acronym == 'Alagoas' or Type_the_state_or_acronym == 'AL' or Type_the_state_or_acronym == 'Rio Grande do Norte' or Type_the_state_or_acronym == 'RN':

                print ('Brazilian state or acronym: %s' % (Type_the_state_or_acronym))
                print ('CPF identification: 555.555.554-55')
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_state_or_acronym == 'Bahia' or Type_the_state_or_acronym == 'BA' or Type_the_state_or_acronym == 'Sergipe' or Type_the_state_or_acronym == 'SE':

                print ('Brazilian state or acronym: %s' % (Type_the_state_or_acronym))
                print ('CPF identification: 666.666.665-66')
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_state_or_acronym == 'Minas Gerais' or Type_the_state_or_acronym == 'MG':

                print ('Brazilian state or acronym: %s' % (Type_the_state_or_acronym))
                print ('CPF identification: 777.777.776-77')
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_state_or_acronym == 'Rio de Janeiro' or Type_the_state_or_acronym == 'RJ' or Type_the_state_or_acronym == 'Espírito Santo' or Type_the_state_or_acronym == 'ES':

                print ('Brazilian state or acronym: %s' % (Type_the_state_or_acronym))
                print ('CPF identification: 888.888.887-88')
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_state_or_acronym == 'São Paulo' or Type_the_state_or_acronym == 'SP':

                print ('Brazilian state or acronym: %s' % (Type_the_state_or_acronym))
                print ('CPF identification: 999.999.998-99')
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

            elif Type_the_state_or_acronym == 'Paraná' or Type_the_state_or_acronym == 'PR' or Type_the_state_or_acronym == 'Santa Catarina' or Type_the_state_or_acronym == 'SC':

                print ('Brazilian state or acronym: %s' % (Type_the_state_or_acronym))
                print ('CPF identification: 000.000.009-00')
                subprocess.run (['sleep 2.5'], shell=True)
                subprocess.run (['clear'], shell=True)

        else:

            print ('Brazilian state or acronym not found...')
            subprocess.run (['sleep 2.5'], shell=True)
            subprocess.run (['clear'], shell=True)

    except:

        pass

def main ():

    try:

        if sys.argv [1] == '-h':

            time.sleep (0.5)
            os.system ('clear')

            print ('python3 CPFidentificationbyBrazilianstates.py [state or acronym]')

            time.sleep (2.5)
            os.system ('clear')

        else:

            Type_the_state_or_acronym = (sys.argv [1])
            function (Type_the_state_or_acronym)

    except:

        usage ()

if __name__ == '__main__':

    main ()

