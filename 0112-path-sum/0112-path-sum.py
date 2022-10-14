# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root: return False
        
        def DFS(root, ts):
            nextLv = []
            if root.left: nextLv.append(root.left)
            if root.right: nextLv.append(root.right)
               
            if ts-root.val == 0 and not nextLv: return True
            elif nextLv:
                fs= False
                for nextNd in nextLv:
                    fs = DFS(nextNd, ts-root.val)
                    if fs: return fs
        
        return DFS(root, targetSum)
        
        
        
            
        