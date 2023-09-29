class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m =len(heights)
        n = len(heights[0])
        diffMat = [[float('inf') for _ in range(n)] for _ in range(m)]
        visit = [[False for _ in range(n)] for _ in range(m)]
        diffMat[0][0] = 0

        def valid(x, y):
            if 0 <= x < m and 0 <= y < n and not visit[x][y]:
                return True
            return False

        hq = [(0,0,0)]
        while hq:
            eff, x, y = heapq.heappop(hq)
            visit[x][y] = True
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                if valid(x+dx, y+dy):
                    max_diff = max(eff, abs(heights[x+dx][y+dy] - heights[x][y]))
                    if diffMat[x+dx][y+dy] > max_diff:
                        diffMat[x+dx][y+dy] = max_diff
                        heapq.heappush(hq, (diffMat[x+dx][y+dy], x+dx, y+dy))
                    
        return diffMat[m-1][n-1]
        


            

