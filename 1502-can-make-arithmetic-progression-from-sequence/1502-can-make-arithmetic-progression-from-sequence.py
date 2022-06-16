class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        n, min_, max_ = len(arr), min(arr), max(arr)
        seen = [False] * n
        plus = (max_ - min_) / (n - 1)
        
        if plus != int(plus): return False
        plus = int(plus)
        if plus == 0: return sum(arr)//n == arr[0]
        
        seen[(arr[0] - min_) // plus] = True
        for i in range(n-1):
            if (arr[i] - arr[i+1]) % plus == 0 and seen[(arr[i+1] - min_) // plus] == False:
                seen[(arr[i+1] - min_) // plus] = True
            else: return False
        
        return True