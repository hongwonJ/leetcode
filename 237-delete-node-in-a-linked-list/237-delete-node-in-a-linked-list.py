# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev_n = node
        next_n = node.next
        
        while next_n.next:
            prev_n.val = next_n.val
            prev_n = next_n
            next_n = next_n.next
        
        prev_n.val = next_n.val
        prev_n.next = None
        