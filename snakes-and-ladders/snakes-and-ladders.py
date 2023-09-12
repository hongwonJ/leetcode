class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2+1)
        label = 1
        columns = list(range(0, n))
        for row in range(n-1, -1, -1):
            for col in columns:
                cells[label] = (row, col)
                label += 1
            columns.reverse()
        dist = [-1 for _ in range(n**2 + 1)] 
        dist[1] = 0
        q = collections.deque([1])
        while q:
            curr = q.popleft()
            for nxt in range(curr+1, min(curr+6, n*n)+1):
                row, col = cells[nxt]
                dest = (board[row][col] if board[row][col] != -1 else nxt)
                if dist[dest] == -1:
                    dist[dest] = dist[curr] + 1
                    q.append(dest)
        return dist[n*n]
                        
        
        
    