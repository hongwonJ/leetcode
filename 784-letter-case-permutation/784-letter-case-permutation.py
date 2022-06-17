class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if len(s) == 1 or s.isdigit():
            if s.isdigit(): return [s]
            elif len(s) == 1: return [s.lower(), s.upper()]
        else:
            ans = []
            i = 0
            while s[i].isdigit(): i += 1
            frontL = s[:i] + s[i].lower()
            frontU = s[:i] + s[i].upper()
            if i+1 < len(s):
                for back in self.letterCasePermutation(s[i+1:]):
                    ans.append(frontL + back)
                    ans.append(frontU + back)
            else:
                ans.append(frontL)
                ans.append(frontU)
            return ans
            
            
            
            
            
            