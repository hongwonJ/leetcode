class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max, n = 0, len(nums)
        i, numz, count = 0, nums.count(0), 0

        while count < numz:
            while i + 1 < n and nums[i] == 1:
                i += 1
            l, r = 1, 1
            while i - (l + 1) > -2 and nums[i - l] == 1: l += 1
            while i + (r + 1) < n+1 and nums[i + r] == 1: r += 1
            if (l - 1) + (r - 1) + 1 > max: max = l + r - 1
            count += 1
            i += 1

        if numz == 0: return n

        return max


        
                
            
        
                    