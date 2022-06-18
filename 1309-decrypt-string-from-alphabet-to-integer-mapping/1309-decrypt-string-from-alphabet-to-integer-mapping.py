class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        i, ans = 0, ''
        while i < len(s):
            if i < len(s) - 2 and s[i + 2] == '#':
                ans += chr(int(s[i:i+2]) + 96)
                i += 3
            else:
                ans += chr(int(s[i]) + 96)
                i += 1
        
        return ans
