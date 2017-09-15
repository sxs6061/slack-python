import itertools
#Find a pair of elements from an array whose sum equals a given number

def sum_array(A,x):
    for num in itertools.combinations(set(A), 2):
        if num[0] + num[1] == x:
            return 1
    return 0


A = [2, 4, 6, 8, 10]
x = 8 # True condition
#x = 3 # False condition
res = sum_array(A, x)
print "exists" if res else "Doesnt exist"
