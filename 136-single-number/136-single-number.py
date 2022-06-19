class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_ = dict()
        for n in nums:
            if n not in dict_: dict_[n] = 1
            else: dict_[n] += 1
        
        for m in dict_:
            if dict_[m] == 1: return m
            
            