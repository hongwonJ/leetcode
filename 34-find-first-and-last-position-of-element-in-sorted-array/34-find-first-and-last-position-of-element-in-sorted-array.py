class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findP(nums: List[int], target: int) -> List[int]:
            a, b = 0, len(nums) - 1
            while a <= b:
                c = (a + b) // 2
                if nums[c] == target: 
                    return a, b, c
                elif nums[c] < target: a = c + 1
                else: b = c - 1
            return -1, -1, -1
        
        s,e,m = findP(nums,target)
        if s == -1: return [-1, -1]        
        
        min_, max_ = -1, -1
        a, b = s, m
        while a <= b:
            c = (a + b) // 2
            if nums[c] == target:
                min_ = c
                b = c - 1
            elif nums[c] < target: a = c + 1
            else: b = c - 1
        
        a, b = m, e
        while a <= b:
            c = (a + b) // 2
            if nums[c] == target:
                max_ = c
                a = c + 1
            elif nums[c] < target: a = c + 1
            else: b = c - 1
                
        return [min_, max_]
    
    