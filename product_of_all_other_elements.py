# product of all other elements in array without division
def product_of_all_other_elements(nums):
    prefix = []
    for n in nums:
        if prefix:
            prefix.append(prefix[-1] * n)
        else:
            prefix.append(n)
    
    suffix = []
    for n in reversed(nums):
        if suffix:
            suffix.append(suffix[-1] * n)
        else:
            suffix.append(n)
    suffix = list(reversed(suffix))

    results = []
    for i in range(len(nums)):
        if i == 0:
            results.append(suffix[i + 1])
        elif i == len(nums) - 1:
            results.append(prefix[i - 1])
        else:
            results.append(prefix[i - 1] * suffix[i + 1])
    
    return results

print(product_of_all_other_elements([3,2,1]))

# product of all other elements in array with division
# def product_of_all_other_elements(arr):
#     # Calculate the total product of all elements in the array
#     total_product = 1
#     for num in arr:
#         total_product *= num

#     # Generate the output array
#     output = []
#     for num in arr:
#         output.append(total_product // num)

#     return output

# # Example usage
# arr = [3,2,1]
# result = product_of_all_other_elements(arr)
# print(result)