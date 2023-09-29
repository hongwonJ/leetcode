from collections import deque
class Solution:
    def valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
            return True
        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotted = deque()
        non_rotted = set()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotted.append((i,j))        
                if grid[i][j] == 1:
                    non_rotted.add((i,j))
        if not non_rotted:
            return 0
        moved = [(1,0),(-1,0),(0,1),(0,-1)]
        t = -1
        while rotted:
            k = len(rotted)
            for _ in range(k):   
                x, y = rotted.popleft()
                for m_x, m_y in moved:
                    x_n, y_n = x + m_x, y + m_y
                    if self.valid(x_n, y_n, grid):
                        rotted.append((x_n, y_n))
                        grid[x_n][y_n] = 2
                        non_rotted.remove((x_n, y_n))
            t += 1
        return t if not non_rotted else -1