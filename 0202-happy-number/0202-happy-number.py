class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])
        while (n > 1):
            tmp = 0
            while (n > 0):
                tmp += (n%10)**2
                n //= 10
            n = tmp
            if n in seen: return False
            seen.add(n)
        else: 
            return True
                
                