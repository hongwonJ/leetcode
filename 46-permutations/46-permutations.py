class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        if n == 1: return [nums]
        else:
            for i in range(n):
                nums[0], nums[i] = nums[i], nums[0]
                rest = self.permute(nums[1:])
                for r in rest:
                    ans += [([nums[0]] + r)]
            return ans