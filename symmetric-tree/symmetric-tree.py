# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lv = deque()
        lv.append(root)
        while lv: 
            n = len(lv)
            for _ in range(n):
                x = lv.popleft()
                if not x: continue
                if x.left: lv.append(x.left)
                else: lv.append(None)
                if x.right: lv.append(x.right)
                else: lv.append(None)
            m = len(lv)
            for i in range(m//2):
                if (not lv[i] and lv[-1-i]) or (not lv[-1-i] and lv[i]): return False
                elif (lv[i] and lv[-1-i]) and (lv[i].val != lv[-1-i].val): return False
        return True