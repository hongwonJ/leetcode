class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 1: return 0
        cur, nex = 0, 1
        pro = 0
        
        while cur < l - 1:
            if prices[cur] < prices[nex]:
                pro += (prices[nex] - prices[cur])
            cur += 1
            nex += 1
        
        return pro
            