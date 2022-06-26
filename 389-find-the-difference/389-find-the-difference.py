class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_ = dict()
        for i in range(len(s)):
            if s[i] in dict_: dict_[s[i]] += 1 
            else: dict_[s[i]] = 1
            
        for i in range(len(t)):
            if t[i] not in dict_ or dict_[t[i]] == 0: return t[i]
            elif dict_[t[i]] > 0: dict_[t[i]] -= 1
            