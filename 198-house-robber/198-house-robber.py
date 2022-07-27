class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        elif len(nums) <= 2: return max(nums)
        else:
            m = (len(nums)-1)//2
            m1 = self.rob(nums[:m]) + self.rob(nums[m+2:])
            m2 = self.rob(nums[:m-1]) + nums[m] + self.rob(nums[m+2:])
            m3 = self.rob(nums[:m]) + nums[m+1] + self.rob(nums[m+3:])
            return max([m1, m2, m3])
        
            