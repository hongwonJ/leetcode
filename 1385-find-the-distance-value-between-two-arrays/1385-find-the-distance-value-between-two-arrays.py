class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        cnt = 0 
        
        for n in arr1:
            a, b = 0, len(arr2) - 1
            sgn = True
            while a <= b:
                c = (a + b)//2
                if -d <= n - arr2[c] <= d:
                    sgn = False
                    break
                elif n - arr2[c] < -d: b = c - 1
                else: a = c + 1
            if sgn: cnt += 1
          
        return cnt
            
     