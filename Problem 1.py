__author__ = 'Jin Zhou'

import math


def MultiplesThreeFive(n):
    # simply sum up the multiples of 3 and multiples of 5
    # minus their intersect, which means the multiples of 15
    # (A or B) = A + B - (A and B) by set theory
    count = 0
    for i in range(3,n,3):
        count += i
    for i in range(5,n,5):
        count += i
    for i in range(15,n,15):
        count -= i
    return count

MultiplesThreeFive(1000)

