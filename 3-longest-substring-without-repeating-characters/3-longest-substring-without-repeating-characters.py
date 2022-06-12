class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans        
        
        
'''
        lst = list(s)
        n = len(lst)
        
        if n == 0: return 0
        
        def longestSub(lst, i):
            if i == 1: return 0, 1, 0
            a, b, c = longestSub(lst,i-1)
            
            if lst[i-1] in lst[c:i-1]:
                while lst[i-1] in lst[c:i-1]: c += 1
                return a, b, c
            elif a == c: return a, i, c
            else:
                if i-c >= b-a: return c, i, c
                else: return a, b, c
        
        a, b, c = longestSub(lst, n)   
        return max(b-a, n-c)
'''