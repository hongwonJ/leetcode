class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums) - 1
        if target < nums[0]: return 0
        if nums[-1] < target: return b + 1
        while a <= b:
            c = (a + b)//2
            if nums[c] < target:
                a = c + 1
                if b < a: return c + 1
            elif nums[c] > target:
                b = c - 1
                if b < a: return c
            else: return c