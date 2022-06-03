# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None: return 0
        
        lv = [[root]]
        
        while lv[-1]:
            lv.append([])
            for node in lv[-2]:
                if node.left: lv[-1].append(node.left)
                if node.right: lv[-1].append(node.right)
                    
        return len(lv) - 1
                
                
        
        