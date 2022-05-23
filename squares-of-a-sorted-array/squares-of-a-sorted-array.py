class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R, sol = [], [], []
        for k in nums:
            if k < 0: L.append(k**2)
            else: R.append(k**2)
        L.reverse()

        if not L: return R
        if not R: return L
        i, j = 0, 0
        while i + j < n:
            if (j == len(R)) or (i < len(L) and L[i] < R[j]):
                sol.append(L[i])
                i += 1
            else:
                sol.append(R[j])
                j += 1
        return sol
