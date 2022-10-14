# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        paths = []
        path = []
        
        def DFS(root, ts, path):
            path.append(root.val)
            nextLv = []
            if root.left: nextLv.append(root.left)
            if root.right: nextLv.append(root.right)
            if ts-root.val == 0 and not nextLv:
                paths.append(path[:])
            elif nextLv:
                for nextNd in nextLv:
                    DFS(nextNd, ts-root.val, path) 
                    path.pop()
        
        if root: DFS(root, targetSum, path)
        
        return paths
        
        
        