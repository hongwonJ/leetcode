class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        stack, seen = [source], set()
        Adj = self.buildAdj(n, edges)

        while stack: 
            x = stack.pop()
            if x == destination: return True
            if x not in seen:
                seen.add(x)
                for y in Adj[x][1:]:
                    if y not in seen: stack.append(y)
                        
        return False
            
    def buildAdj(self, n:int, edges: List[List[int]]) -> List[List[int]]:
        Adj = [[i] for i in range(n)]
        for e in edges:
            Adj[e[0]].append(e[1])
            Adj[e[1]].append(e[0])
        return Adj