class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        A, M = [0], [0]
        max_ = 0
        for i in range(1, n):
            if i == 1:
                M.append(prices[i-1])
                if prices[i] > M[i]:
                    A.append(prices[i] - M[i])
                else:
                    A.append(0)
            else: 
                # Setting list M
                if prices[i-1] < M[i-1]: M.append(prices[i-1])
                else: M.append(M[i-1])
                # Setting list A
                if prices[i] > M[i]: A.append(prices[i] - M[i])
                else: A.append(0)
            # find Maximum
            if A[i] > max_: max_ = A[i]
        return max_
                