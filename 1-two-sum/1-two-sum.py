class Solution:
    def twoSum(self, nums: list(), target: int) -> list():
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in nums[i+1:]:
                return(i,nums[i+1:].index(diff)+i+1)
