class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a, b = 0, len(arr) - 1
        while a <= b:
            c = (a + b) // 2
            if arr[c] - (c + 1) == k:
                while c - 1 >= 0 and arr[c - 1] == arr[c] - 1: c -= 1
                return arr[c] - 1
            elif arr[c] - (c + 1) < k:
                a = c + 1
            else:
                b = c - 1
        if arr[c] - (c + 1) < k:
            while c + 1 < len(arr) and arr[c + 1] == arr[c]: c += 1
            return arr[c] + (k - (arr[c] - (c + 1)))
        else:
            while c - 1 >= 0 and arr[c - 1] == arr[c]: c -= 1
            return arr[c] - 1 - (arr[c] - (c + 1) - k)
        
            
        
                
                