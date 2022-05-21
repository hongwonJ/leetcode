# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

               
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        curr = head

        while curr:
            prev = dummy

            while prev.next and prev.next.val < curr.val:
                prev = prev.next
                
            next = curr.next
            # insert the current node to the new list
            curr.next = prev.next
            prev.next = curr

            # moving on to the next iteration
            curr = next

        return dummy.next

                