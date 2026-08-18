"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Input: nums = [1, 2, 3, 3]

Output: true

"""

class Solution:
    def hasDups(self, array):
        return len(set(array)) < len(array)

nums = [1, 2, 3, 3]
sol = Solution()
print(sol.hasDups(nums))