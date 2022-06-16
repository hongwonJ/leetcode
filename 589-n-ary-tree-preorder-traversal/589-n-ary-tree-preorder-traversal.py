"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        order = []
        
        return self.addOrder(root, order)
        
    def addOrder(self, root, order):
        if not root: return root
        order.append(root.val)
        if root.children:
            for childNode in root.children:
                self.addOrder(childNode, order)
        return order
            
            
        