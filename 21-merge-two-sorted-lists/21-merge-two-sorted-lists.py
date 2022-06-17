# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1, p2 = ListNode(), ListNode()        
        p1.next, p2.next = list1, list2
        ans = p1
        if not list1: return list2
        
        while p1.next or p2.next:
            if not p2.next or (p1.next and p1.next.val <= p2.next.val): p1 = p1.next
            else:
                tmp = ListNode(p2.next.val)
                tmp.next = p1.next
                p1.next = tmp
                p1, p2 = p1.next, p2.next
        return ans.next
            
            
        