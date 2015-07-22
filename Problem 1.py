__author__ = 'Jin Zhou'

import math

def MultiplesThreeFive(n):
    sum_35 = 0
    for i in range(3,n,3):
        sum_35 += i
    for i in range(5,n,5):
        sum_35 += i
    for i in range(15,n,15):
        sum_35 -= i
    return sum_35

MultiplesThreeFive(1000)
