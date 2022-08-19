class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        while i < n-1:
            if nums[i] != nums[i+1]:
                i += 1
                j += 1
                nums[j] = nums[i]
            else:
                i += 1
        return j+1