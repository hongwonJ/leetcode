class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1: return True
        n = len(nums)
        for i in range(n-1,0,-1):
            isbroken = True
            for k in range(i-1,-1,-1):
                if k+nums[k] >= i: isbroken = False
                if not isbroken: break
            if isbroken: return False
        return True