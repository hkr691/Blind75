"""
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

    The left subtree of every node contains only nodes with keys less than the node's key.
    The right subtree of every node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees are also binary search trees.

Example 1:

Input: root = [2,1,3]

Output: true

"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isWithinBounds(root, float("-inf"), float("inf"))
    
    def isWithinBounds(self, node, lowerbound, upperbound):
        if not node:
            return True
        if not(lowerbound < node.val < upperbound):
            return False
        return self.isWithinBounds(node.left, lowerbound, node.val) and self.isWithinBounds(node.right, node.val, upperbound)