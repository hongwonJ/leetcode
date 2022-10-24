class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        ts = sum(nums)
        ss = ts // 2
        if ts % 2 != 0: return False
        
        dt = [-1 for _ in range(ss+1)] 
        dt[0] = 0
               
        for i in range(n): 
            for k in range(ss, 0, -1):
                if k == ss and dt[ss] != -1: return True
                if k - nums[i] >= 0 and dt[k-nums[i]] != -1: dt[k] = dt[k-nums[i]] + 1
                
        
        return False