from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        D = [] 
        for i in range(m):
            D.append([])
            for j in range(n):
                if grid[i][j] == 2: D[i].append(0)
                elif grid[i][j] == 1: D[i].append(float(inf))
                else: D[i].append(None)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    self.DFS(i,j,m,n,grid,D)
        print(D)
        
        max_dpth = 0
        for i in range(m):
            for j in range(n):
                if D[i][j] is None: continue
                elif D[i][j] == float(inf): return -1
                elif D[i][j] > max_dpth: max_dpth = D[i][j]
                
        return max_dpth
        
    def DFS(self,i,j,m,n,grid,D):
        dpth, stack,seen = 0, deque(), set()
        stack.append([i,j,0])
        while stack:
            i, j, d = stack.popleft()
            if D[i][j] > d: D[i][j] = d
            if i-1 >= 0 and grid[i-1][j] == 1 and (i-1, j) not in seen:
                stack.append([i-1, j, d+1])
                seen.add((i-1, j))
            if i+1 < m and grid[i+1][j] == 1 and (i+1, j) not in seen:
                stack.append([i+1, j, d+1])
                seen.add((i+1, j))
            if j-1 >= 0 and grid[i][j-1] == 1 and (i, j-1) not in seen:
                stack.append([i, j-1, d+1])
                seen.add((i, j-1))
            if j+1 < n and grid[i][j+1] == 1 and (i, j+1) not in seen:
                stack.append([i, j+1, d+1])
                seen.add((i, j+1))
            
        
        