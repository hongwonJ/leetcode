# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findDes(root, x): 
            path = []
            while True:
                if x.val == root.val:
                    path.append(root)
                    return path
                elif x.val < root.val:
                    path.append(root)
                    root = root.left
                else: 
                    path.append(root)
                    root = root.right
        
        ppath = findDes(root, p)
        qpath = findDes(root, q)
        
        while ppath:
            x = ppath.pop()
            if x in qpath: return x
                
            
            
        
                
            
                
                    
            