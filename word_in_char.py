# Print the largest word from words, formed of characters from chars

import itertools
words = [ "abc" , "baa" , "caan" , "an" , "banc", "baanc" ]
chars = [ "a" , "a" , "n" , "c" , "b"]
l = list()
for word in words:
    l.extend( set(''.join(i) for i in (itertools.product(chars, repeat = len(word)))) )
print '\n'.join(w for w in set(l).intersection(words) if len(w) == len(max(set(l).intersection(words), key=len)))
