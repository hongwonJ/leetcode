# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        rec = [0, n]
        self.binSearch(rec)
        return rec[1]
    
    def binSearch(self, rec: List[int]) -> None:
        c = (rec[0] + rec[1] + 1)//2
        if isBadVersion(c):
            rec[1] = c
            if rec[0] + 1 == c: return
            else: self.binSearch(rec)
        else:
            rec[0] = c
            self.binSearch(rec)
        