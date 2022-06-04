# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return False
        traLst = []
        
        def traverse(root, traLst):
            if root.left: traverse(root.left, traLst)
            traLst.append(root.val)
            if root.right: traverse(root.right, traLst)
            return traLst
        
        traLst = traverse(root, traLst)
        for i in range(len(traLst) - 1):
            if traLst[i] >= traLst[i + 1]: return False
        
        return True
            
 