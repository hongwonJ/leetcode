from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        D = [[float(inf) for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                self.findDist(i,j,m,n,mat,D)
        
        for i in range(m-1,-1,-1):
            for j in range(n):
                self.findDist(i,j,m,n,mat,D)
        
        for i in range(m):
            for j in range(n-1,-1,-1):
                self.findDist(i,j,m,n,mat,D)
        
        for i in range(m-1, -1, -1):
            for j in range(n-1,-1,-1):
                self.findDist(i,j,m,n,mat,D)
                        
        return D
        
    def findDist(self, x, y, m, n, mat, D):
        if mat[x][y] == 0: D[x][y] = 0
        else:
            l = D[x-1][y] if x-1 >= 0 else float(inf)
            r = D[x+1][y] if x+1 < m else float(inf)
            u = D[x][y+1] if y+1 < n else float(inf)
            d = D[x][y-1] if y-1 >= 0 else float(inf)
            D[x][y] = min(l, r, u, d) + 1
            