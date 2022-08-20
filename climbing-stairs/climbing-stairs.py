class Solution:
    def climbStairs(self, n: int) -> int:
        x = [None for _ in range(n+1)]
        x[0] = x[1] = 1
        for i in range(2, n+1):
            x[i] = x[i-1] + x[i-2]
        return x[n]
            
        
            