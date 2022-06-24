from collections import deque
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int):
        m, n = len(mat), len(mat[0])
        if m*n != r*c: return mat
        
        dq = deque()
        for i in range(m):
            for j in range(n):
                dq.append(mat[i][j])
        ans = []
        for i in range(r):
            ans.append([])
            for j in range(c):
                ans[i].append(dq.popleft())
        return ans
            