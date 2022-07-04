# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev_head = ListNode()
        prev_head.next= head
        curr = prev_head
        fast = prev_head
        
        while fast and fast.next:
            curr = curr.next
            fast = fast.next.next
        
        half = curr
        prev_n = curr
        curr = curr.next
        if curr: next_n = curr.next
        else: return True
        
        while curr:
            if prev_n != half: curr.next = prev_n
            else: curr.next = None
            half.next = curr
            if next_n: prev_n, curr, next_n = curr, next_n, next_n.next
            else: prev_n, curr = curr, next_n
        
        while half:
            prev_head = prev_head.next
            half = half.next
            if half and half.val != prev_head.val: return False

        return True