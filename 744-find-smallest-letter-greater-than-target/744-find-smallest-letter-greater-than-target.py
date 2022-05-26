class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        a, b = 0, len(letters) - 1
        pos, sgn = -1, False
        i = 0
        while a <= b:
            c = (a + b) // 2
            if target == letters[c]:
                pos = c
                sgn = True
                break
            elif target < letters[c]:
                b = c - 1
                sgn = False
            else:
                a = c + 1
                sgn = True
            pos = c
        if sgn:
            i = 1
            while letters[(pos+i) % len(letters)] == target:
                i += 1            
        return letters[(pos+i) % len(letters)]
            
        
        
            