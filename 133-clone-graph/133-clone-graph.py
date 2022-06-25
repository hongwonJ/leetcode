"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        pair = dict()
        seen = set()

        def DFS(node):
            if not node: return None
            seen.add(node)
            copy = Node(node.val)
            pair[node] = copy
            for adj_node in node.neighbors:
                if adj_node not in seen:
                    DFS(adj_node)
            for adj_node in node.neighbors:
                copy.neighbors.append(pair[adj_node])
            return copy
        
        return DFS(node)
        