class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxSet, n = set(), len(nums)
        for i in range(n):
            if len(maxSet) < 3 or nums[i] > min(maxSet): maxSet.add(nums[i])
            if len(maxSet) > 3: maxSet.remove(min(maxSet))
        return min(maxSet) if len(maxSet) == 3 else max(maxSet)

                
            
            
        