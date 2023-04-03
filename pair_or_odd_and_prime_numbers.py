
# coding: UTF-8

# pair_or_odd_and_prime_numbers.py

number = int (input ('Type the number: '))
zero = 0

class numbers:

    def __init__ (self, number, zero):

        self.number = number
        self.zero = zero

    def pair_or_odd_and_prime_numbers (self):

        for value in range (2, self.number + 1):

            if self.number % value == 0:

                self.zero += 1

        if self.number == 2:

            return ('number %s is prime and pair' % (self.number))

        elif self.zero == 1:

            return ('number %s is prime and odd' % (self.number))

        else:

            return ('number %s is not prime and pair' % (self.number))

result = numbers (number, zero)

print (result.pair_or_odd_and_prime_numbers ())
