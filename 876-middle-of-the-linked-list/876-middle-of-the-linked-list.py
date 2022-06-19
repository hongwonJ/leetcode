# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        init = ListNode()
        init.next = head
        slow = init
        fast = init
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow if not fast else slow.next
