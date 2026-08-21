"""
You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6]

Output: 36

Explanation: The bars at indices 1 and 7 have heights 7 and 6. The container has width 7 - 1 = 6 and height min(7, 6) = 6, so it can store 6 * 6 = 36 units of water. This is the maximum possible area.

Example 2:

Input: height = [2,2,2]

Output: 4
"""

class Solution():
    def maxArea(self, heights):
        maxWater = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            currWater = min(heights[r], heights[l]) * (r - l)
            maxWater = max(currWater, maxWater)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return maxWater

sol = Solution()
height = [1,7,2,5,4,7,3,6]
height1 = [2,2,2]

print(sol.maxArea(height))
print(sol.maxArea(height1))