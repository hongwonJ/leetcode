class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sumL = [[sum(r), i] for i, r in enumerate(mat)]
        sumL.sort()
        
        return [sumL[i][1] for i in range(k)]
        
        