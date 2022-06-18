class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict_ = dict()
        i = 0
        for c in order:
            dict_[c] = i
            i += 1
        
        for k in range(len(words) - 1):
            if words[k] == words[k+1]: continue
            j = 0
            while j < min(len(words[k]),len(words[k+1])) and words[k][j] == words[k+1][j]:
                j += 1
            if j > (len(words[k+1]) - 1): return False
            elif j > (len(words[k]) - 1): continue
            if dict_[words[k][j]] > dict_[words[k+1][j]]: return False
        
        return True
            