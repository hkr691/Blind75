"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
"""

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        
        for i, num in enumerate(nums):
            if (target - num) in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i   #order of these ops important - pitfall!

nums1, target1 = [3,4,5,6], 7
nums2, target2 = [4,5,6], 10

sol = Solution()
print(sol.twoSum(nums1, target1))
print(sol.twoSum(nums2, target2))