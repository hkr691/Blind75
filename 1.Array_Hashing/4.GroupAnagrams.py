"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

Input: strs = ["x"]

Output: [["x"]]

Example 3:

Input: strs = [""]

Output: [[""]]
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        
        for s in strs:
            hashmap[self.getKey(s)].append(s)
        return list(hashmap.values())
        
    
    def getKey(self, s):
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        return tuple(count)
        
sol = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(sol.groupAnagrams(strs)) 