#returns a list of non-unique elements

data = [int(i) for i in raw_input().split()]
print ([ num for num in data if(data.count(num) > 1) ])
