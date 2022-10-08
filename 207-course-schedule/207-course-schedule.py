class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = dict()
                
        for edge in prerequisites:
            if edge[1] not in adj: adj[edge[1]] = set([edge[0]])
            adj[edge[1]].add(edge[0])
            
        n = len(adj)
        seen = set()
        cycle = False
            
        for key in adj.keys():
            if key not in seen:
                chain = set()
                cycle = self.DFS(adj, key, seen, chain, cycle)
                if cycle is True: return False
        return True
        
    def DFS(self, adj, key, seen, chain, cycle):
        seen.add(key)
        chain.add(key)
        if key in adj:
            for adj_p in adj[key]:
                if adj_p in chain: return True
                if adj_p not in seen:
                    cycle = self.DFS(adj, adj_p, seen, chain, cycle)
                    if cycle: return cycle
                    chain.remove(adj_p)
        return False