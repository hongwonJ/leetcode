class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if n < m or m == 0: return -1
        for i in range(n):
            if haystack[i] == needle[0]:
                right = True
                for j in range(m):
                    if i+j >= n or haystack[i+j] != needle[j]: right = False
                if right: return i
        return -1