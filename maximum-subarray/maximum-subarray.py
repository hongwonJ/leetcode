class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        memo = {}
        def dp(i):
            if i == n-1: return nums[i]
            if i not in memo:
                memo[i] = max(dp(i+1) + nums[i], nums[i])
            return memo[i]
        
        return max([dp(i) for i in range(n-1, -1, -1)])
                
        
        