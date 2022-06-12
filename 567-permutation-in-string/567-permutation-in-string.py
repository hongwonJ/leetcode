class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        alph = 'abcdefghijklmnopqrstuvwxyz'
        n1, n2 = len(s1), len(s2)
        char1, char2 = {}, {}
        
        if n1 > n2: return False
        
        for i in range(26):
            char1[alph[i]] = 0
            char2[alph[i]] = 0
        
        for i in range(n1):
            char1[s1[i]] += 1
        
        for i in range(n1):
            char2[s2[i]] += 1
                
        def compareDict(d1, d2):
            for i in range(26):
                if d1[alph[i]] != d2[alph[i]]: return False
            return True
        
        k = 0            
        while k < n2-n1+1:
            if k > 0:
                char2[s2[k-1]] -= 1
                char2[s2[k + n1-1]] += 1
            if compareDict(char1, char2): return True
            k += 1
            
        return False
    