__author__ = 'januschou'

def EvenFibonacci(n):
    num1 = 1
    num2 = 1
    num3 = 2
    evensum = 0

    while num1<n and num2<n and num3<n:
        evensum += num3
        num1 = num2+num3
        num2 = num3+num1
        num3 = num1+num2

    return evensum

EvenFibonacci(4000000)

