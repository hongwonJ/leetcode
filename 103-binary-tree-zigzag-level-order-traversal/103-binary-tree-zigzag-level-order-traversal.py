# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        level, ans = [[root]], [[root.val]]
        right = True
        
        while level[-1]:
            level.append([])
            ans.append([])
            for node in reversed(level[-2]):    
                if right: self.rightToLeft(node, level, ans)
                if not right: self.leftToRight(node, level, ans)
            right = not right
            
        return ans[:-1]
                    
    def rightToLeft(self, node, level, ans):
        if node.right:
            level[-1].append(node.right)
            ans[-1].append(node.right.val)
        if node.left: 
            level[-1].append(node.left)
            ans[-1].append(node.left.val)
    
    def leftToRight(self, node, level, ans):
        if node.left:
            level[-1].append(node.left)
            ans[-1].append(node.left.val)
        if node.right: 
            level[-1].append(node.right)
            ans[-1].append(node.right.val)
        
                
                
                
            
            