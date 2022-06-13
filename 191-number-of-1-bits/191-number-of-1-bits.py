class Solution:
    def hammingWeight(self, n: int) -> int:
        
        cnt = 0
        mask = 1
        for _ in range(32):
            if (mask & n): cnt += 1
            mask <<=1
        return cnt 