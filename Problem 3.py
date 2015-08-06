__author__ = 'Jin Zhou'

import math

# Determine whether a integer is prime number
def IsPrime(n):
    #starting from 3 and only considering odd numbers,
    for i in xrange(3,int(math.floor(math.sqrt(n))),2):
        if n % i == 0:
            return False
    return True


def LargestPrimeFactor(n):
    LargestFactor = 0
    for i in xrange(3,int(math.floor(math.sqrt(n))),2):
        if n % i == 0 and IsPrime(i):
            LargestFactor = i

    if LargestFactor == 0:
        return n
    else:
        return  LargestFactor


LargestPrimeFactor(600851475143)