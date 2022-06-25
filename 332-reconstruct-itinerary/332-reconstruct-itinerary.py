class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        Adj, visit = dict(), dict()
        stack = ["JFK"]
        paths, path = [], []
        n = len(tickets)
            
        for route in tickets:
            if route[0] not in Adj: Adj[route[0]] = [route[1]]
            else:
                Adj[route[0]].append(route[1])
                Adj[route[0]].sort()
            if tuple(route) not in visit: visit[tuple(route)] = 1
            else: visit[tuple(route)] += 1
        
        def DFS(place):
            if paths: return
            path.append(place)
            if len(path) == n+1:
                paths.append(path.copy())
                return
            if place not in Adj:
                return
            for adj_place in Adj[place]:
                if paths: return
                if visit[(place, adj_place)] > 0:
                    visit[(place, adj_place)] -= 1
                    DFS(adj_place)
                    path.pop()
                    visit[(place, adj_place)] += 1
                    
        DFS("JFK")
        
        return paths[0]