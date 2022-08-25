class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(n-1-2*i):
                matrix[i+j][n-1-i], matrix[n-1-i][n-1-i-j], matrix[n-1-i-j][i], matrix[i][i+j] = matrix[i][i+j], matrix[i+j][n-1-i], matrix[n-1-i][n-1-i-j], matrix[n-1-i-j][i]
                
        return
