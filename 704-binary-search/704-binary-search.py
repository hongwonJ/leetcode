class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums) -1
        while a <= b:
            c = (a+b)//2
            if target < nums[c]: b = c - 1
            elif target > nums[c]: a = c + 1
            else: return c
        return -1
        