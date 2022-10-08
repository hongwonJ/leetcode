class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        
        n = len(s)
        distChar = dict()
        si, maxlen = 0, float('-inf')
        
        for ei in range(n):
            if s[ei] not in distChar: distChar[s[ei]] = 1
            else: distChar[s[ei]] += 1
            if len(distChar) > k:
                while len(distChar) > k:
                    if distChar[s[si]] > 1: distChar[s[si]] -= 1
                    else: distChar.pop(s[si])
                    si += 1
            maxlen = max(maxlen, ei - si + 1)
                        
        return maxlen
                    
            
            
        
        
        
        