class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        for _ in range(32):
            x = n & 1
            n >>= 1
            m <<= 1
            m += x
        return m
        