class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_ = 0
        marked = [False] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not marked[i * n + j]:
                    con = self.DFS(grid, i, j, marked)
                    if  con > max_: max_ = con
        return max_
    
    def DFS(self, grid: List[List[int]], i:int, j:int, marked: List[int]) -> int:    
        marked[i*len(grid[0]) + j] = True
        if grid[i][j] == 1:
            con = 1
            if i > 0 and not marked[(i-1)*len(grid[0]) + j]:
                con += self.DFS(grid, i-1, j, marked)
            if i < len(grid)-1 and not marked[(i+1)*len(grid[0]) + j]:
                con += self.DFS(grid, i+1, j, marked)
            if j > 0 and not marked[i*len(grid[0]) + j-1]:
                con += self.DFS(grid, i, j-1, marked)
            if j < len(grid[0])-1 and not marked[i*len(grid[0]) + j+1]:
                con += self.DFS(grid, i, j+1, marked)    
            return con
        else:
            return 0
            
        
            
        