class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n: return mat
        res, lst = [], []

        for i in range(m):
            for j in range(n):
                lst.append(mat[i][j])

        for i in range(r):
            res.append([])
            for j in range(c):
                res[i].append(lst[i * c + j])

        return res
                
                
        