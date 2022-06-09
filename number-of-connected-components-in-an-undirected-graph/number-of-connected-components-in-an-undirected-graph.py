class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)
        for e in edges: uf.union(e[0], e[1])

        return uf.getCount()


class UnionFind:
    def __init__(self, size):
        self.p = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
    
    def find(self, x):
        if self.p[x] == x: return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]
        
    def union(self, x, y):
        pX = self.find(x)
        pY = self.find(y)
        if pX != pY:
            if self.rank[pX] > self.rank[pY]:
                self.p[pY] = pX
            elif self.rank[pX] < self.rank[pY]:
                self.p[pX] = pY
            else:
                self.p[pY] = pX
                self.rank[pX] += 1
            self.count -= 1
            
    def getCount(self):
        return self.count