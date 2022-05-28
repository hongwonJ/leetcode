class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rst, dict = [], {}
        for n in nums: dict[n] = True
        return [i+1 for i in range(len(nums)) if i+1 not in dict]

    
'''
        numSet = sorted(set(nums))
        rst, j = [], 0
        for i in range(1, len(nums) + 1):
            if i == numSet[j]: j += 1
            else: rst.append(i)
        return rst
'''

