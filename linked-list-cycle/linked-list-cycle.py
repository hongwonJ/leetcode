class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        pre_head = ListNode()
        pre_head.next = head
        if not head: return False
        
        slow = pre_head
        fast = slow.next
        
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        
        return False if not (fast and fast.next) else True
