class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minbuy = [prices[0] for _ in range(n)]
        max_ = 0
        for i in range(1, n):
            minbuy[i] = min(minbuy[i-1], prices[i])
            max_ = max(max_, prices[i] - minbuy[i])
        return max_
            
            
        
        
                