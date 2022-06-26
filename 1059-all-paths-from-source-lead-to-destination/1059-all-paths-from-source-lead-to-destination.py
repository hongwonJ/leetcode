class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.Adj = self.buildAdj(edges)
        self.Visited = [False] * n
        self.sign = True
        if destination in self.Adj: return False
        self.DFS(source, destination)
        
        return self.sign
        
    def buildAdj(self, edges):
        Adj = dict()
        for depart, destin in edges:
            if depart not in Adj: Adj[depart] = [destin]
            else: Adj[depart].append(destin)
        return Adj
    
    def DFS(self, node, destination):
        if not self.sign: return
        self.Visited[node] = True
        if node not in self.Adj:
            if node != destination: self.sign = False
            return
        else:
            node_visited = []
            for adj_node in self.Adj[node]:
                node_visited.append(self.Visited[adj_node])
                if not self.Visited[adj_node]:
                    self.DFS(adj_node, destination)
                    self.Visited[adj_node] = False
                if all(node_visited):
                    self.sign = False
                    return
            
                
                