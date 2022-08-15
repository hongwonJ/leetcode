class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        max_ = 0
        
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] > max_: max_ = matrix[i][j]
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    k1 = matrix[i-1][j-1]
                    k2 = matrix[i-1][j]
                    k3 = matrix[i][j-1]
                    if k1*k2*k3 > 0:
                        matrix[i][j] = min(k1, k2, k3) + 1
                    if matrix[i][j] > max_: max_ = matrix[i][j]
        
        return max_*max_
