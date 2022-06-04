class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum_Sub, max_Sub = 0, float('-inf')
        
        for i in range(len(nums)):
            sum_Sub += nums[i]
            if sum_Sub > max_Sub: max_Sub = sum_Sub
            if sum_Sub < 0: sum_Sub = 0
        
        return max_Sub
        
            
                
            
        