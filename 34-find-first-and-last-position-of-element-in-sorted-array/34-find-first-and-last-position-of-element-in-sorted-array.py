class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def tSearch(a: int, b: int, nums: list, target: float):
            while a <= b:
                c = (a + b) // 2
                if target < nums[c]: b = c -1
                elif nums[c] < target: a = c + 1
                else: return True, c
            return False, c
    
        t_dex = tSearch(0, len(nums) - 1, nums, target) if len(nums) > 0 else (False, -1)
        
        if not t_dex[0]: return [-1, -1]
        else:
            start = tSearch(0, t_dex[1] - 1, nums, target - 0.5)[1] if t_dex[1] > 1 else 0
            if nums[start] != target: start += 1 
            end = tSearch(t_dex[1] + 1, len(nums) - 1, nums, target + 0.5)[1] if t_dex[1] < len(nums) -1 else len(nums) - 1
            if nums[end] != target: end -= 1

        return [start,end]




