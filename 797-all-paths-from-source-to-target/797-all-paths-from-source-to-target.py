class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths, path = [], []
        
        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path.copy())
                return
            
            for next_node in graph[node]:
                dfs(next_node)
                path.pop()
        dfs(0)
        return paths
        