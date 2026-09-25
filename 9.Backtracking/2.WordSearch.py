"""
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:

Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] == '#' or board[r][c] != word[i]):
                return False
            
            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                  dfs(r - 1, c, i + 1) or
                  dfs(r, c + 1, i + 1) or
                  dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAT"
sol = Solution()
print(sol.exist(board, word))