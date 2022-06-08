class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findMin(nums: List[int], target: int) -> List[int]:
            min_ = -1
            a, b = 0, len(nums) - 1
            while a <= b:
                c = (a + b) // 2
                if nums[c] == target: 
                    min_ = c
                    b = c - 1
                elif nums[c] < target: a = c + 1
                else: b = c - 1
            return min_
        
        def findMax(nums: List[int], target: int) -> List[int]:
            max_ = -1
            a, b = 0, len(nums) - 1
            while a <= b:
                c = (a + b) // 2
                if nums[c] == target: 
                    max_ = c
                    a = c + 1
                elif nums[c] < target: a = c + 1
                else: b = c - 1
            return max_
        
        min_ = findMin(nums, target)
        if min_ == -1: return [-1, -1]
        max_ = findMax(nums, target)
        
        return [min_, max_]