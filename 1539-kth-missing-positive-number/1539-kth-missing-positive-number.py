class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a, b = 0, len(arr) - 1
        while a <= b:
            c = (a + b) // 2
            if arr[c] - (c + 1) < k: a = c + 1
            else: b = c - 1
        return a + k
        
        
        
                
                