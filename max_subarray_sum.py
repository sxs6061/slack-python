# calcluate the max sum of subarray
def max_subarray_sum(array):
    max_ending_here = max_so_far = 0 
    for x in array:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# extending this for wrap-around
def min_subarray_sum(array):
    min_ending_here = min_so_far = 0 
    for x in array:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far

def max_circular_sum(array):
    max_subarray_sum_wraparound = sum(array) - min_subarray_sum(array)
    return max(max_subarray_sum(array), max_subarray_sum_wraparound)


array = [8, -1, 3, 4]
result = max_subarray_sum(array)
result_extension = max_circular_sum(array) # extension
print(result)
print(result_extension)