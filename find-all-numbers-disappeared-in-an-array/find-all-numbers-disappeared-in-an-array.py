class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet = sorted(set(nums))
        rst, j = [], 0
        for i in range(1, len(nums) + 1):
            if j < len(numSet) and i == numSet[j]: j += 1
            else: rst.append(i)
        return rst
