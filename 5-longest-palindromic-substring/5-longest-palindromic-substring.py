class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dt=[[False for _ in range(n)] for _ in range(n)]
        max_ = [1, 0, 0]
        
        for i in range(n):
            dt[i][i] = True
            if i < n-1 and s[i] == s[i+1]:
                dt[i][i+1] = True
                max_[:] = [2,i,i+1]
            
        for k in range(2,n):
            for i in range(n-k):
                if (s[i] == s[i+k] and dt[i+1][i+k-1]):
                    dt[i][i+k] = True
                    if k+1 > max_[0]: max_[0:3] = [k+1,i,i+k]
        
        return s[max_[1]:max_[2]+1]
     