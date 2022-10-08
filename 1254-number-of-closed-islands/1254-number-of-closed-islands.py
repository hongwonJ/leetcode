class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        count, visit = 0, set()
        
        def DFS(i, j, cl):
            if (i, j) not in visit: visit.add((i, j))
            if (i==0 or i==m-1 or j==0 or j==n-1): cl = False
            l, r, u, d = max(j-1, 0), min(j+1, n-1), max(i-1, 0), min(i+1, m-1)
            adjs = [(i,l),(i,r),(u,j),(d,j)]
            for (adj_i, adj_j) in adjs:
                if (adj_i, adj_j) not in visit and grid[adj_i][adj_j] == 0:
                    cl = DFS(adj_i, adj_j, cl)
            return cl
        
        for i in range(m):
            for j in range(n):                
                if grid[i][j] == 0 and (i, j) not in visit:
                    cl = DFS(i, j, True)
                    if cl: count += 1
    
        return count
            
        
                
                
            
                
            
                    
                
                
        