__author__ = 'Jin Zhou'


# Largest palindrome product

PalindromeProduct = 0

# Simply search possible ranges of two 3-digits factors

for i in xrange(900,1000):
    for j in xrange(900,1000):
        ProductStr = str(i*j)
        # To see whether the reversed string is the same as orginal
        if ProductStr == ProductStr[::-1] and PalindromeProduct < (i*j):
            PalindromeProduct = i*j

print PalindromeProduct