from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == '1' and (i,j) not in seen):
                        self.BFS(grid, m, n, i, j, seen)
                        ans += 1
        return ans
                
    def BFS(self, grid:List[List[str]], m:int, n:int, i:int, j:int, seen):
        stack = deque()
        stack.append((i,j))
        while stack:
            k = len(stack)
            for _ in range(k):
                s, t = stack.popleft()
                seen.add((s,t))
                if (0 <= s - 1) and grid[s-1][t] == '1' and (s-1, t) not in seen:
                    stack.append((s-1, t))
                    seen.add((s-1, t))
                if s + 1 < m and grid[s+1][t] == '1' and (s+1, t) not in seen:
                    stack.append((s+1, t))
                    seen.add((s+1, t))
                if 0 <= t - 1 and grid[s][t-1] == '1' and (s, t-1) not in seen:
                    stack.append((s, t-1))
                    seen.add((s, t-1))
                if t + 1 < n and grid[s][t+1] == '1' and (s, t+1) not in seen:
                    stack.append((s, t+1))
                    seen.add((s, t+1))
                
                
        
        
        