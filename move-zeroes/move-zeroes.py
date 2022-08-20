class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nzp = 0
        
        for i in range(len(nums)):
            if nums[i] != 0: 
                nums[nzp], nums[i] = nums[i], nums[nzp]
                nzp += 1
                
        