class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = dict()
        for c in t:
            if c in dic: dic[c] += 1
            else: dic[c] = 1
        for c in s:
            if c not in dic or dic[c] == 0: return False
            else: dic[c] -= 1
        for c in dic:
            if dic[c] != 0: return False
        return True
        
            
            
            