class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = ''
        for c in s:
            if c.isalpha() or c.isdigit(): chars += c
        
        n = len(chars)
        
        for i in range(n//2):
            if chars[i].lower() != chars[-1-i].lower(): return False
        return True
            