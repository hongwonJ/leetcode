# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
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
                