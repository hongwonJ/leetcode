class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt  = 0 
        for i in arr1:
            sgn = False
            for j in arr2:
                if (i - j) <= d and (i - j) >= -d:
                    sgn = True
            if sgn == False: cnt += 1

        return cnt
            