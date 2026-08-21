"""
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3

Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        l, r = 0, 0
        maxLen = 0
        hashSet = set()
        
        #right pointer used to expand on seeing unseen character
        #left pointer contracts the window in case dups encountered
        while r < len(s):
            if s[r] not in hashSet:
                hashSet.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r += 1
            else:
                hashSet.remove(s[l])
                l += 1
                
        return maxLen

s1 = "zxyzxyz"
s2 = "xxxx"
sol = Solution()
print(sol.lengthOfLongestSubstring(s1))
print(sol.lengthOfLongestSubstring(s2))