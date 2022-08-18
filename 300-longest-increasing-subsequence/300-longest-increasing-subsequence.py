class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        
        for i in range(n-1, -1, -1):
            for k in range(n-1, i, -1):
                if nums[i] < nums[k] and dp[i] < dp[k] + 1:
                    dp[i] = dp[k] + 1
                
        return max(dp)