"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]
"""
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        counter = {}
        heap = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        if len(counter) == k:
            return list(counter.keys())
        
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
            #heapq.heappushpop(heap, (count, num))
        print(f"counter: {counter}")    
        return [tup[1] for tup in heap]

sol = Solution()
nums, k = [1,2,2,3,3,3], 2
nums1, k1 = [7, 7], 1
#print(sol.topKFrequent(nums, k))
print(sol.topKFrequent(nums1, k1))