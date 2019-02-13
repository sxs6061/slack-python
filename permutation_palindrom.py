# Given a string, determine whether any permutation of it is a palindrome.
# For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. 
# daily should return false, since there's no rearrangement that can form a palindrome.
#
import itertools

data = "carrace"
print bool(any({ bool(''.join(i)[::-1] == ''.join(i)) for i in itertools.permutations(data) }))