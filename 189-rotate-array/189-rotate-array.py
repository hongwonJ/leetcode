class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        if k == 0: return
        nums[:k], nums[k:] = nums[l-k:], nums[:l-k]