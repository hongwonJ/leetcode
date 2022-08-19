class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        memo = {}
        # s[:i]까지를 조합할 수 있는 경우 True, 아니면 False
        def dp(i):
            if i == 0: return True
            if i not in memo:
                memo[i] = False
                for j in range(0, i+1):
                    if dp(j) and (s[j:i] in wordDict): memo[i] = True
            return memo[i]

        return dp(n)
        
        
            
            
            
        
            
            
            