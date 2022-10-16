class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        
        for i in range(n):
            while nums[i] != i+1:
                if nums[i] != nums[nums[i]-1]:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                else:
                    break
                    
        for i in range(n):
            if nums[i] != i+1: ans.append(i+1)
    
        return ans
                