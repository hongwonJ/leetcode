class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_, pro_ = 0, 1
        
        while n > 0:
            n, r = divmod(n, 10)
            sum_ += r
            pro_ *= r
        
        return pro_ - sum_ 