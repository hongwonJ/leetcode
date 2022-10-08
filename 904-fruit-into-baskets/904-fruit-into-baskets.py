from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        si = 0
        maxnum = float('-inf')
        basket = defaultdict(int)
        
        for ei in range(n):
            basket[fruits[ei]] += 1
            if len(basket) > 2:
                while len(basket) > 2:
                    basket[fruits[si]] -= 1
                    if basket[fruits[si]] == 0: basket.pop(fruits[si])
                    si += 1
            maxnum = max(maxnum, ei-si+1)
        return maxnum
                    
                    
            
            
            