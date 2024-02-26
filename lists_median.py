# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5

import bisect
nums1 = [1, 2]
nums2 = [3, 4]

[ bisect.insort(nums1, num) for num in nums2 ]
print(sum(nums1[len(nums1)//2-1:len(nums1)//2+1])/2.0, nums1[len(nums1)//2])[len(nums1) % 2]