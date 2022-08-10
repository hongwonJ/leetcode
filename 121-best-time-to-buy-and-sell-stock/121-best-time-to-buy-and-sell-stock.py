class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        A = [0 for _ in range(n)]
        M = [0 for _ in range(n)]
        for i in range(n-1, -1, -1):
            if i == n-1: M[i] = prices[i]
            else: 
                if prices[i] > M[i+1]:
                    M[i] = prices[i]
                else:
                    M[i] = M[i+1]
                if prices[i] < M[i]:
                    A[i] = M[i] - prices[i]
        return max(A)
                
        
            