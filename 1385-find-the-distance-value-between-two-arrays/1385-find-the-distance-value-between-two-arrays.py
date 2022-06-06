class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        cnt = 0 
        
        def findMin(n, arr):
            a, b = 0, len(arr) - 1
            while a <= b:
                c = (a + b) // 2
                if n - arr[c] == d: return c
                elif n - arr[c] < d: b = c - 1   
                else: a = c + 1
            return a
            
        def findMax(n, arr):
            a, b = 0, len(arr) - 1
            while a <= b:
                c = (a + b) // 2
                if arr[c] - n == d: return c
                elif arr[c] - n < d: a = c + 1
                else: b = c - 1
            return b
    
        for i in range(len(arr1)):
            iMax, iMin = findMax(arr1[i], arr2), findMin(arr1[i], arr2)
            if iMax < iMin: cnt += 1
          
        return cnt
            