class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dic = dict()
        
        for s in magazine: 
            if s in dic: dic[s] += 1
            else: dic[s] = 1
            
        for s in ransomNote:
            if s not in dic or dic[s] == 0: return False
            else: dic[s] -= 1
        
        return True