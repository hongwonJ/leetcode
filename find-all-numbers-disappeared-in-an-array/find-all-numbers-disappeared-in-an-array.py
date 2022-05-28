class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rst, dict = [], {}
        for n in nums: dict[n] = True
        return [i+1 for i in range(len(nums)) if i+1 not in dict]
