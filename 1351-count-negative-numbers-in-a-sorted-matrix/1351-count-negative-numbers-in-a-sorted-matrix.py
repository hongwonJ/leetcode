class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        def findNeg(lst: List[int], e: int) -> int:
            a, b = 0, e - 1
            while a <= b:
                c = (a + b) // 2
                if lst[c] == 0:
                    while c+1 < e and lst[c+1] == 0:
                        c += 1
                    return c
                elif lst[c] < 0: b = c - 1
                else: a = c + 1
            return b
        
        m, n = len(grid), len(grid[0])
        
        Zs = []
        Zs.append(findNeg(grid[0], n))
        for i in range(1, m):
            Zs.append(findNeg(grid[i], Zs[i-1] + 1))
        
        ans = 0
        for i in range(m):
            ans += n - Zs[i] - 1
        print(Zs)
        
        return ans
