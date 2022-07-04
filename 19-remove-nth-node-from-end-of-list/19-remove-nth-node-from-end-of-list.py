# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev_head = ListNode()
        prev_head.next = head
        fast = prev_head
        slow = prev_head
        
        for _ in range(n):
            fast = fast.next
        
        if fast: 
            while fast.next:
                fast = fast.next
                slow = slow.next
        
        slow.next = slow.next.next
        
        return prev_head.next
        
        