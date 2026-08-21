"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true

Example 2:

Input: s = "([{}])"

Output: true

Example 3:

Input: s = "[(])"

Output: false
"""

class Solution:
    def isValid(self, s):
        if not s:
            return False
        
        hashmap = {'(': ')', 
                   '[': ']',
                   '{': '}'}
        stack = []
        
        for char in s:
            if char in hashmap:
                stack.append(char)
            elif stack and char == hashmap[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack

sol = Solution()
s1 = "[]"
s2 = "([{}])"
s3 = "[(])"

print(sol.isValid(s1))
print(sol.isValid(s2))
print(sol.isValid(s3))