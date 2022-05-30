class Solution:
    def firstUniqChar(self, s: str) -> int:
        dup_dic = dict()
        for i in s:
            if i not in dup_dic: dup_dic[i] = True
            else: dup_dic[i] = False
        for i in range(len(s)):
            if dup_dic.get(s[i]): return i
        return -1
        
            
            
        
            
        