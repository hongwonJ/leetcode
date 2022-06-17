class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def count(n):
            if n == 1: return 1
            elif n == 2: return 2
            elif n not in memo:
                memo[n] = count(n-1) + count(n-2)
            return memo[n]
        
        return count(n)
          