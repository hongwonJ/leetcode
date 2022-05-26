class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n: return mat
        res = []

        for i in range(m*n):
            s, t = divmod(i, c)
            u, v = divmod(i, n)
            if t == 0: res.append([])
            res[s].append(mat[u][v])

        return res
                
        