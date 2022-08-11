class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        
        def dp(n: int) -> int:
            if n == 1: return 0
            if n == 2: return min(cost[0], cost[1])
            if n not in memo:
                memo[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
            return memo[n]
        
        return dp(n)
            
        
