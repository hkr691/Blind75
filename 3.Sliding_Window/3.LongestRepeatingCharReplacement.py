"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4

Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
"""

class Solution:
    def characterReplacement(self, s, k):
        hashmap = {}
        l, r = 0, 0
        maxFreq, maxLen = 0, 0
        
        while r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, hashmap[s[r]])
            currWindow = r - l + 1
            if currWindow - maxFreq > k:
                hashmap[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen

s1, k1 = "XYYX", 2
s2, k2 = "AAABABB", 1

sol = Solution()
print(sol.characterReplacement(s1, k1))
print(sol.characterReplacement(s2, k2))