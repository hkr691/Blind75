"""
Kth Smallest Integer in BST


Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

    The left subtree of every node contains only nodes with keys less than the node's key.
    The right subtree of every node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees are also binary search trees.


Example 1:

Input: root = [2,1,3], k = 1

Output: 1
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr[k - 1]