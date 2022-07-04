class Solution:
    def deleteNode(self, node):
        prev_n = node
        next_n = node.next
        
        while next_n.next:
            prev_n.val = next_n.val
            prev_n = next_n
            next_n = next_n.next
        
        prev_n.val = next_n.val
        prev_n.next = None
