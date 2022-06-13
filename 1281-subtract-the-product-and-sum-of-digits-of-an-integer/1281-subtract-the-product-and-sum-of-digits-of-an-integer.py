class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_, pro_ = 0, 1
        
        q = 1
        while q > 0:
            q, r = divmod(n, 10)
            sum_ += r
            pro_ *= r
            n = q
        
        return pro_ - sum_ 