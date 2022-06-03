# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
    
        self.traverse(root, output)
        
        return output
                
            
    def traverse(self, root: Optional[TreeNode], output: List[int]) -> List[int]:
        if root is not None:
            output.append(root.val)
            if root.left: self.traverse(root.left, output)
            if root.right: self.traverse(root.right, output)
        return output    