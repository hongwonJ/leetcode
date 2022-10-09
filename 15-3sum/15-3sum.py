class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        def twoSum(i, target):
            resid = dict()
            an = []
            dupi = dict()
            for k in range(i+1, n):
                if nums[k] not in resid:
                    resid[target - nums[k]] = nums[k]
                    dupi[target - nums[k]] = False
                    dupi[nums[k]] = False
                elif nums[k] in resid and not dupi[target - nums[k]] and not dupi[nums[k]]:
                    an.append([nums[k], resid[nums[k]]])
                    dupi[nums[k]] = True
                    dupi[target - nums[k]] = True
                    
            return an
        
        ans = []
        for i in range(n-2):
            an = []
            if i == 0 or nums[i] != nums[i-1]:
                an = twoSum(i, -nums[i])
            if an:
                for a in an: 
                    a.append(nums[i])
                    ans.append(a)
                
        return list(ans)
            
        
        