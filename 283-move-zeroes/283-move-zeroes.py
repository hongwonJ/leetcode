class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, n = 0, len(nums)
        
        for j in range(n):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        
        for k in range(1, n-i+1): nums[-k] = 0
        