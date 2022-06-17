class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if len(triangle) == 1: return triangle[0][0]
        Adj = self.buildAdj(triangle)
        triList = self.toList(triangle)
        d = [float(inf) for _ in triList]
        d[0] = triangle[0][0]
        
        for u in Adj: 
            for v in Adj[u]:
                if d[v] > d[u] + triList[v]: d[v] = d[u] + triList[v]
        
        print(Adj)
        print(triList)
        print(d)
        
        w = len(triangle[-1])
        return min(d[-w:])
        
    def buildAdj(self, triangle: List[List[int]]) -> int:
        h, Adj = len(triangle), dict()
        for i in range(h):
            w = len(triangle[i])
            for j in range(w):
                TIS = 0
                for k in range(i+1): TIS += k
                TIS += j
                if i + 1 < h: Adj[TIS] = [TIS + i + 1, TIS + i + 2]
        return Adj
    
    def toList(self, triangle: List[List[int]]) -> List[int]:
        h, triList = len(triangle), []
        for i in range(h):
            w = len(triangle[i])
            for j in range(w):
                triList.append(triangle[i][j])
        return triList
        
        

            