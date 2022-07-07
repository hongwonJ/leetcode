# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        BSTlist = []
        self.DFS(root, BSTlist)
        for i in range(len(BSTlist) - 1):
            if BSTlist[i] >= BSTlist[i+1]: return False
        return True
        
    def DFS(self, root, BSTlist):
        if root.left: self.DFS(root.left, BSTlist)
        BSTlist.append(root.val)
        if root.right: self.DFS(root.right, BSTlist)