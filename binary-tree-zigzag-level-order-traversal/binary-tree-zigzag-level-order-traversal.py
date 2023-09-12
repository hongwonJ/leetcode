# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque([root])
        ans = []; left = False
        if not root: 
            return []
        while que:
            k = len(que)
            ans.append([])
            left = not left
            for _ in range(k):
                nd = que.popleft()
                if nd:
                    ans[-1].append(nd.val)
                    if nd.left: que.append(nd.left)                        
                    if nd.right: que.append(nd.right)
            if not left: ans[-1].reverse()
                    
        return ans

        

        
                
                
                
            
            