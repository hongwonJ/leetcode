class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        s, n = 0, len(nums)
        zc = 0
        maxlen = float('-inf')
        for e in range(n):
            if nums[e] == 0: zc += 1
            while zc > k:
                if nums[s] == 0: zc -= 1
                s += 1
            maxlen = max(maxlen, e-s+1)
        return maxlen
                    
                