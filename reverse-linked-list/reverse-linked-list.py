class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        ans = ListNode()
        
        while curr:
            tmp = ListNode(curr.val)
            ans.next, tmp.next = tmp, ans.next
            curr = curr.next
            
        return ans.next
