class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        dp = [[0]*n for _ in range(amount+1)]
        
        for csum in range(1, amount + 1):
            for idx in range(n):
                res = csum - coins[idx]
                if res == 0: dp[csum][idx] = 1
                elif res < 0: dp[csum][idx] = float('inf')
                else:
                    dp[csum][idx] = min([dp[res][prev_idx] for prev_idx in range(n)]) + 1
        
        ans = min(dp[amount])
        return  ans if ans < float('inf') else -1
    
      
                
            
            
            