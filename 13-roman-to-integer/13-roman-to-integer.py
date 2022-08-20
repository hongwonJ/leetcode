class Solution:
    def romanToInt(self, s: str) -> int:
        romDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        ans = 0
        for i in range(n):
            if s[i] == "I" and i + 1 < n and (s[i+1] == "V" or s[i+1] == "X"): 
                ans -= 1
            elif s[i] == "X" and i + 1 < n and (s[i+1] == "L" or s[i+1] == "C"): 
                ans -= 10
            elif s[i] == "C" and i + 1 < n and (s[i+1] == "D" or s[i+1] == "M"):
                ans -= 100
            else:
                ans += romDict[s[i]]

        return ans
            
            