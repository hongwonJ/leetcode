class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_ = [0, 0]
        for i in range(n):
            r = 0
            while (0 <= i-r and i+r<n):
                if s[i-r] == s[i+r]:
                    if 2*r+1 > max_[1]-max_[0]+1:
                        max_ = i-r, i+r
                    r += 1
                else:
                    break
        for i in range(n-1):
            if s[i] == s[i+1]:
                r = 0
                while (0 <= i-r and i+1+r<n):
                    if s[i-r] == s[i+1+r]:
                        if 2*r+2 > max_[1]-max_[0]+1:
                            max_ = i-r, i+1+r
                        r += 1
                    else:
                        break
        return s[max_[0]:max_[1]+1]
