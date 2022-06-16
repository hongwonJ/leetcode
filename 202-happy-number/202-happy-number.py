class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            sum_ = 0
            while n > 0:
                n, r = divmod(n, 10)
                sum_ += r*r
            if sum_ == 1: return True
            if sum_ in seen: return False
            else: seen.add(sum_)
            n = sum_
        
            
            