class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        m = self.decInterval(nums)[0]
        if nums[0] <= target: a, b  = 0, m
        else: a, b = m + 1, len(nums) - 1
        while a <= b:
            c = (a + b)//2
            if nums[c] == target: return c
            elif nums[c] < target: a = c+1
            else: b = c-1
        return -1
        
    
    def decInterval(self, nums:List[int]) -> [int, int]:
        ans = [0, len(nums)-1]
        if nums[ans[0]] < nums[ans[1]]: return [len(nums)-1,0]
        
        while ans[1] - ans[0] > 1:
            a, b = ans[0], ans[1]
            c = (a+b)//2
            if nums[a] > nums[c]: ans = [a,c]
            elif nums[c] > nums[b]: ans = [c, b]
                
        return ans
    
    
    