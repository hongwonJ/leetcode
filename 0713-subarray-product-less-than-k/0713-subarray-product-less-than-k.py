class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        i, j = 0, 0 
        prod = 1
        j_increased= True
        while i < n and j < n:

            if nums[j] >= k:
                j += 1
                i = j
                prod = 1
                continue
            if j_increased: prod *= nums[j]
            if prod < k:
                ans += j-i+1
                j += 1
                j_increased= True
            else:
                prod //= nums[i]
                i += 1
                j_increased = False
                    
        return ans
        
