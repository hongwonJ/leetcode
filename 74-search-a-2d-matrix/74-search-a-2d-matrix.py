class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        a, b = 0, m*n-1
        while a <= b:
            c = (a+b)//2
            c_row, c_col = divmod(c, n)
            if matrix[c_row][c_col] == target: return True
            elif matrix[c_row][c_col] < target: a = c+1
            else: b = c-1
        return False

                
     