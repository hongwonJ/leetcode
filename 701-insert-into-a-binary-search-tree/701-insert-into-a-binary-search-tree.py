# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        
        rst = root
        instN = TreeNode(val)
        sgn = False
        
        if not root: return instN
        
        while root: 
            if root.val < val:
                prev = root
                root = root.right
                sgn = True
            else:
                prev = root
                root = root.left
                sgn = False
        
        if sgn: prev.right  = instN
        else: prev.left = instN
            
        return rst
        