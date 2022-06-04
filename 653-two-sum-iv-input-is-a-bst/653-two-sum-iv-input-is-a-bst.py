# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        if not root: return False
        
        Lstack, Rstack = [], []
        Lx, Rx = root, root
        
        def makeLeft(Lstack, node):
            Lstack.append(node)
            while node:
                if node.left: Lstack.append(node.left)
                node = node.left
        
        def makeRight(Rstack, node):
            Rstack.append(node)
            while node:
                if node.right: Rstack.append(node.right)
                node = node.right
        
        def nextLeft(Lstack):
            prev = Lstack.pop()
            if prev.right: makeLeft(Lstack, prev.right)
            return prev
            
        def nextRight(Rstack):
            prev = Rstack.pop()
            if prev.left: makeRight(Rstack, prev.left)
            return prev
        
        makeLeft(Lstack, Lx)
        makeRight(Rstack, Rx)
        
        a, b = nextLeft(Lstack), nextRight(Rstack)
        
        while a.val < b.val:
            if a.val + b.val == k: return True
            elif a.val + b.val < k: a = nextLeft(Lstack)
            else: b = nextRight(Rstack)
        
        return False
        
                
        
'''
        if root is None: return False
        
        dq = deque()
        dq.append(root)
        set_ = set()
        
        while dq:
            root = dq.popleft()
            set_.add(root.val)
            if root.left:
                dq.append(root.left)
                set_.add(root.left.val)
            if root.right:
                dq.append(root.right)
                set_.add(root.right.val)
        
        for i in set_:
            if 2*(k-i) != k and k-i in set_: return True
        return False
'''
                