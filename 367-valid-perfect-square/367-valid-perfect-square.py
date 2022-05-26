class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a, b = 0, num
        while a <= b:
            c = (a + b) // 2
            if c*c < num: a = c + 1
            elif c*c > num: b = c - 1
            else: return True
        return False