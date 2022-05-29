class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        words = s.split(' ')
        for word in words:
            ans.append(''.join(reversed(list(word))))
        return ' '.join(ans)
        
                
                
            
            
        