# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a, b, minBad = 0, n, -1
        while a <= b:
            c = (a + b)//2
            if isBadVersion(c) == False: a = c + 1
            else:
                minBad = c
                b = c - 1
        return minBad
                

                