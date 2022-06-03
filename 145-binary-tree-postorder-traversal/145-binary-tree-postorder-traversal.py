# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None: return []
        
        stack, output = [root], []
        
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left: stack.append(root.left)
            if root.right: stack.append(root.right)
        
        output.reverse()
        
        return output