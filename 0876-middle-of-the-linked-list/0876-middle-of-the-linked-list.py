# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp = ListNode(val = 0, next = head)
        s = sp
        f = sp
        while f is not None:
            s = s.next
            if f.next: f = f.next.next
            else: f = f.next
        return s
        
    
            