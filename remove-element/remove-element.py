class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j,k = 0,0
        while j < len(nums):
            if nums[j] == val:
                k += 1
            else: 
                nums[j - k]  = nums[j]
            j += 1
        return len(nums) - k
                