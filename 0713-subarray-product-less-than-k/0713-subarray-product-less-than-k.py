class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        i, j = 0, 0 
        
        prod = nums[0]
        while i < n and j < n:
            if prod < k:
                j += 1
                ans += j-i
                if j < n: prod *= nums[j]
            elif prod >= k and i < j:
                prod //= nums[i]
                i += 1
            else: 
                i += 1
                j += 1
                if j < n: prod = nums[j]
            
        return ans
        
