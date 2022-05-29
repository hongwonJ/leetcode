class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        sp, ep = 0, len(nums) - 1
        smp = self.pSearch(sp, ep, nums, target)
        emp = smp
        while smp > 0 and nums[smp-1] == target:
            smp = self.pSearch(sp, smp - 1, nums, target)
        sp = smp
        while emp < len(nums) - 1 and nums[emp+1] == target:
            emp = self.pSearch(emp + 1, ep, nums, target)
        ep = emp

        return [sp, ep]

    def pSearch(self, a: int, b: int, nums: List[int], target: float) -> int:
        while a <= b:
            c = (a + b) // 2
            if target < nums[c]: b = c - 1
            elif nums[c] < target: a = c + 1
            else: return c
        return -1
    


