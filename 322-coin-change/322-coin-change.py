class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        if n == 0: return -1
        if amount == 0: return 0
        
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for csum in range(1, amount + 1):
            for c in coins:
                if csum - c >= 0 and dp[csum-c] + 1 < dp[csum]:
                    dp[csum] = dp[csum-c] + 1

        return  dp[amount] if dp[amount] < float('inf') else -1
    
     