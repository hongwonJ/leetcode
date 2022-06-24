class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        m = (n - 1)**2 + 1
        Adj = dict()
        
        Adj[0] = graph[0]
        for lv in range(n - 2):
            for nd in range(1, n):
                if graph[nd]: Adj[lv*15 + nd] = [(lv + 1)*15 + k for k in graph[nd]]
        
        paths = [[[0]]]
        for lv in range(n):
            paths.append([])
            for path in paths[-2]:
                if path[-1] in Adj:
                    for adj_x in Adj[path[-1]]:
                        n_path = path + [adj_x]
                        paths[-1].append(n_path)
        
        ans = []
        
        for lvpaths in paths:
            for path in lvpaths:
                if path[-1] % 15 == n-1:
                    path = [x % 15 for x in path]
                    ans.append(path)

        return ans
                    
                
   