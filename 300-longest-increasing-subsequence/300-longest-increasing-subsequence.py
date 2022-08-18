class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        memo = {n-1: 1}
        
        def dp(i):
            if i not in memo:
                ans = 1
                for k in range(n-1, i, -1):
                    if nums[i] < nums[k] and ans < dp(k) + 1: ans = dp(k) + 1
                memo[i] = ans
            return memo[i]
        
        ans = max([dp(i) for i in range(n-1, -1, -1)])
        return ans