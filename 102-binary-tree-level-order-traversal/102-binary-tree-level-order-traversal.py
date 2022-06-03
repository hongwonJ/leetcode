# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: return []
        
        lv = [[root]]
        lval = [[root.val]]
        
        
        while lv[-1]:
            if lv[-1] is None: break
            lv.append([])
            lval.append([]) 
            for x in lv[-2]:
                if x.left:
                    lv[-1].append(x.left)
                    lval[-1].append(x.left.val)
                if x.right: 
                    lv[-1].append(x.right)
                    lval[-1].append(x.right.val)
            
        return lval[:-1]
        
                    
            
        
        
        