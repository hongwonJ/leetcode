class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        trow = -1
        for i in range(m):
            if matrix[i][0] <= target and target <= matrix[i][n-1]:
                trow = i
                break
        if trow == -1: return False
        else:
            a, b = 0, n-1
            while a <= b:
                c = (a+b)//2
                if matrix[trow][c] == target: return True
                elif matrix[trow][c] < target: a = c+1
                else: b = c-1
            return False
                
                
     