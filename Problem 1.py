__author__ = 'Jin Zhou'

import math

def MultiplesThreeFive(n):
    # simply sum up the multiples of 3 and multiples of 5
    # minus their intersect, which means the multiples of 15
    # (A or B) = A + B - (A and B) by set theory
    sum = 0
    for i in range(3,n,3):
        sum += i
    for i in range(5,n,5):
        sum += i
    for i in range(15,n,15):
        sum -= i
    return sum

MultiplesThreeFive(1000)

