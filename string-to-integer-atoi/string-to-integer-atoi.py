class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()
        n = len(s)
        digits = ''
        mark = True
        

        for i in range(n):
            if i == 0 and s[i] == '-': mark = False
            elif i == 0 and s[i] == '+': continue 
            elif s[i].isdigit(): digits += s[i]
            else: break
        
        if digits:
            digits = int(digits)
            if not mark: digits *= -1
        else: digits = 0
        
        if digits > 2**31 - 1: digits = 2**31-1
        elif digits < -2**31: digits = -2**31
        
        return digits
            
        
        