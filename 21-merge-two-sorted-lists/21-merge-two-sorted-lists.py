# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None: return list2
        if list2 is None: return list1
            
        if list1.val <= list2.val:
            i = k = list1
            j = list2
        else: 
            i = k = list2
            j = list1
            
        while i is not None and j is not None:
            if i.next is not None and i.next.val > j.val:
                cnode = ListNode()
                cnode.val = j.val
                cnode.next = i.next
                i.next = cnode
                i = i.next
                j = j.next
            elif i.next is None:
                i.next = j
                break
            else: i = i.next

        return k
            
                
                
                
                
                
        
        