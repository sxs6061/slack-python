# Given n numbers, find the greatest common denominator between them.
# For example, given the numbers [42, 56, 14], return 14.
#
def gcd(a, b): # library(fractions) function for GCD in python
    while b:
        a, b = b, a%b
    return a

L = [42, 56, 14, 7]
print reduce((lambda x, y: gcd(x,y)), L) # apply gcd to sequential pairs of values in a list
