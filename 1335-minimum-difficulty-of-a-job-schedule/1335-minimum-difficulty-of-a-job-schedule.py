class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
                
        max_ = [[0]*n for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                max_[i][j] = max(jobDifficulty[i:j+1])
    
        memo = {}
        def dp(i: int, cd: int) -> int:
            if cd == d: return max_[i][n-1]
            if (n-i) < (d-cd+1): return -1
            elif (n-i) == (d-cd): return sum(jobDifficulty[i:])
            if (i,cd) not in memo:
                memo[(i, cd)] = min([(dp(j, cd+1) + max_[i][j-1]) for j in range(i+1, n-(d-cd)+1)])
            return memo[(i, cd)]
        
        return dp(0, 1)
     