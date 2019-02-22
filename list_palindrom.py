# Given a list of words, find all pairs of unique indices such that the concatenation of 
# the two words is a palindrome.
# For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
#
L = ["code", "edoc", "da", "d"]
print [ (i, L.index(v)) for i,u in enumerate(L) for j,v in enumerate(L[i+1:]+L[:i]) if u+v == v[::-1]+u[::-1] ]
