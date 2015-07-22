__author__ = 'januschou'

def EvenFibonacci(n):
    '''
    Since two odds make an even number,
    the even number will always appear after two odds.
    In this case, simply adopt 3 vars to keep track of the even num.
    '''
    # initialization
    num1 = 1
    num2 = 1
    num3 = 2
    evensum = 0

    while num1<n and num2<n and num3<n:
        # only sum up the even number
        evensum += num3
        num1 = num2+num3
        num2 = num3+num1
        num3 = num1+num2

    return evensum

EvenFibonacci(4000000)

