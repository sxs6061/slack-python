# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
#
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target-num], i]
            dic[num] = i

# Driver Code 
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 18
    res = Solution().twoSum(nums, target)
    print(res)
