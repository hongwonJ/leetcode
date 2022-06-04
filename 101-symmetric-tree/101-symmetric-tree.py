# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        Lstack, Rstack = [], []
        Lval, Rval = [], []
        if root.left:
            Lstack.append(root.left)
            Lval.append(root.left.val)
        if root.right:
            Rstack.append(root.right)
            Rval.append(root.right.val)
        
        for x in Lstack:
            if x.left:
                Lstack.append(x.left)
                Lval.append(x.left.val)
            else: Lval.append(None)
            if x.right:
                Lstack.append(x.right)
                Lval.append(x.right.val)
            else: Lval.append(None)
        
        for x in Rstack:
            if x.right:
                Rstack.append(x.right)
                Rval.append(x.right.val)
            else: Rval.append(None)
            if x.left:
                Rstack.append(x.left)
                Rval.append(x.left.val)
            else: Rval.append(None)
        
        return True if Lval == Rval else False
            
            
        