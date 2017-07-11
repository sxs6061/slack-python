first, second = ("one,two,three", "four,five,one,two,six,three")
print ','.join(sorted(set([s for s in (first.split(',')+second.split(',')) if((first.split(',')+second.split(',')).count(s) > 1)])))
