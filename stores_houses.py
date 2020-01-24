# Stores and Houses: find the closest store for a given house
# Example 1:

# Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
# Output: [5, 11, 16]
# Explanation: 
# The closest store to the house at location 5 is the store at the same location.
# The closest store to the house at location 10 is the store at the location 11.
# The closest store to the house at location 17 is the store at the location 16.

houses = [5, 10, 17]
stores = [1, 5, 20, 11, 16]
print [min(stores, key=lambda x:abs(x-house)) for house in houses]