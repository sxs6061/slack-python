# smaller elements to right
# def smaller_count_naive(array):
#     result = []
#     for i, num in enumerate(array):
#         count = sum(val < num for val in array[i + 1:])
#         result.append(count)
#     return result

import bisect

def smaller_count(array):
    result = []
    seen = []

    # smaller element to the left
    # for num in array:
    #     i = bisect.bisect_right(seen, num)
    #     result.append(i)
    #     bisect.insort(seen, num)

    # return result

    for num in reversed(array):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort(seen, num)

    return list(reversed(result))

array = [3, 4, 9, 6, 1]
result = smaller_count(array)
print(result)