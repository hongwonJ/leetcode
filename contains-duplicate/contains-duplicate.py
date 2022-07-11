class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums = set()
        for n in nums:
            setNums.add(n)
        return True if len(nums) > len(setNums) else False
        