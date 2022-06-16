class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        ans, diff = False, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff ==0:
                    diff += 1
                    char1, char2 = s1[i], s2[i]
                elif diff == 1:
                    diff += 1
                    ans = (s1[i] == char2 and s2[i] == char1)
                else: return False
        return ans
        
    