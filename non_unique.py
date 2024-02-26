# returns a list of non-unique elements
# i/p: 1 2 3 4 3
# o/p: [3, 3]

data = [int(i) for i in raw_input().split()]
print([ num for num in data if(data.count(num) > 1) ])
