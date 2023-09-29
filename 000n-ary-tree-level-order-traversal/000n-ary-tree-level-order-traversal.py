"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans
        que = collections.deque([root])
        while que:
            lv = []
            k = len(que)
            for _ in range(k):
                node = que.popleft()
                lv.append(node.val)
                for child in node.children:
                    que.append(child)
            ans.append(lv[:])
        return ans
            