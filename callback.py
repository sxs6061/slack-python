def func_a(numbers, callback):
    
    # conventional method with callback
    # results = []
    # for i in numbers:
    #     results.append(callback(i))
    # return results
    
    # return ([callback(i) for i in numbers]) # same using list comprehension

    # return map(lambda i : callback(i), numbers) # redundant use of lambdas

    return map(callback, numbers) # same using maps


def func_b(number):
     return number + 2

def func_c(number):
     return number * 2

print func_a([1,2,3,4], func_b) #=> [3, 4, 5, 6]
print func_a([1,2,3,4], func_c) #=> [2, 4, 6, 8]