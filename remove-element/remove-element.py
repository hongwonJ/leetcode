class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        cnt = []
        for i in range(len(nums)):
            if nums[i] == val:
                k += 1
            cnt.append(k)
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i - cnt[i]] = nums[i]
        return len(nums) - k
                