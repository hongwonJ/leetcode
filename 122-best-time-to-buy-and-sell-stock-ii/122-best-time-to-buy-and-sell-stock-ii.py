class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 1: return 0
        cur, nex = 0, 1
        pro, buy = 0, -1
        
        while cur < l:
            if cur == l - 1:
                if buy >= 0: pro += (prices[cur] - buy)
                return pro
            if buy < 0:
                if prices[cur] < prices[nex]:
                    buy = prices[cur]    
            else: 
                if prices[cur] >= prices[nex]:
                    pro += (prices[cur] - buy)
                    buy = -1
            cur += 1
            nex += 1
            