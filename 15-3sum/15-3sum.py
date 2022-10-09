class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        def twoSum(i, target):
            an = []
            k = i+1
            p = n-1
            while k < p:
                if nums[k] + nums[p] > target: p-= 1
                elif nums[k] + nums[p] < target: k+= 1
                else:
                    an.append([nums[k], nums[p]])
                    p -= 1
                    k += 1
                    while k < p and nums[k] == nums[k-1]:
                        k += 1
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
            
        
        