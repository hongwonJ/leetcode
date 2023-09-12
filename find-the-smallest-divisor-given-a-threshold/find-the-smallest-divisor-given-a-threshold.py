import math

class Solution:
    def divsum(self, divisor, nums):
        total = 0
        for num in nums:
            total += math.ceil(num/divisor)
        return total

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        s, l = 1, nums[-1]
        while s < l:
            m = (s+l)//2
            total = self.divsum(m, nums)
            if total <= threshold:
                l = m
            else:
                s = m + 1
        return s

