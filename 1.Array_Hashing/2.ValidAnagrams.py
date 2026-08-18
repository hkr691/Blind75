"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false
"""

class Solution:
    def isValidAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            counter[char] = counter.get(char, 0) - 1
        for value in counter.values():
            if value != 0:
                return False
        return True

s1, t1 = "racecar", "carrace"
s2, t2 = "jar", "jam"
sol = Solution()
print(sol.isValidAnagram(s1, t1))
print(sol.isValidAnagram(s2, t2))