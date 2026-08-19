"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]

Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
"""

class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return nums
        
        n = len(nums)
        res = [1] * n
        prefix = 1
        
        for i in range(1, n):
            prefix *= nums[i - 1]
            res[i] = prefix
        
        postfix = 1
        for i in range(n - 2, -1, -1):
            postfix *= nums[i + 1]
            res[i] *= postfix
        
        return res

nums = [1,2,4,6]
nums1 = [-1,0,1,2,3]
sol = Solution()
print(sol.productExceptSelf(nums))
print(sol.productExceptSelf(nums1))