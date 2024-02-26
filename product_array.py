# Given an array of integers, return a new array such that each element at index i 
# of the new array is the product of all the numbers in the original array except the one at i.

# i/p: [1, 2, 3, 4, 5], o/p [120, 60, 40, 30, 24]. 
# i/p: [3, 2, 1], o/p [2, 3, 6].

# A = [3, 2, 1]
A = [1, 2, 3, 4, 5]
print([ reduce((lambda x, y: x * y), A[:i]+A[i+1:]) for i in range(len(A)) ])
