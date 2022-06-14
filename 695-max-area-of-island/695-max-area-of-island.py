class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_ = 0
        seen = set()
        
        def area(i,j):
            if (i,j) in seen: return 0
            seen.add((i,j))
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                return 1 + area(i+1, j) + area(i-1, j) + area(i, j-1) + area(i, j+1)
            else:
                return 0
            return 0
           
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in seen:
                    con = area(i, j)
                    if  con > max_: max_ = con
                        
        return max_