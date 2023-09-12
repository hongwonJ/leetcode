class Solution:
    def is_divisible(self, threshold, sweetness, k):
        num_chunk = 0
        sum_chunk = 0
        for piece in sweetness:
            if sum_chunk < threshold:
                sum_chunk += piece
            if sum_chunk >= threshold:
                num_chunk += 1
                sum_chunk = 0
            if num_chunk >= k+1:
                return True
        return False
            
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        s, l = min(sweetness), sum(sweetness)//(k+1)+1
        while s < l:
            m = (s+l)//2
            divisible = self.is_divisible(m, sweetness, k)
            if not divisible:
                l = m
            else:
                s = m + 1
        return s - 1