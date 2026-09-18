"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]

Example 2:

Input: head = []

Output: []
"""

class Solution:
    def reverse_linked_list(self, head):
        curr, prev = head, None
        
        while curr:
            next_node = curr.next  #tail of the list
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

