# Determine whether there exists a one-to-one character mapping from one string s1 to another s2 (Isomorphic).
# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
#
def is_isomorphic(s, t):
     if len(s) != len(t): return False
     dic = {}
     for i in range(len(s)):
          sChar = s[i]
          tChar = t[i]
          if dic.has_key(sChar):
               if dic.get(sChar) != tChar: return False
          else:
               if tChar in dic.values(): return False
               dic.setdefault(sChar, tChar)
     return True


s = "aba" #abc
t = "baa" #bcd

print is_isomorphic(s, t)
