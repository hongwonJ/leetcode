import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        rc_sum = 0
        
        while rc_sum < 2*n - 1:
            if rc_sum < n:
                r, c = 0, rc_sum
                for _ in range(rc_sum + 1):
                    heap.append(matrix[r][c])
                    r += 1
                    c -= 1
            else: 
                r, c = rc_sum - n + 1, n - 1
                for _ in range(2*n - rc_sum - 1):
                    heap.append(matrix[r][c])
                    r += 1
                    c -= 1
            rc_sum += 1
        
        heapq.heapify(heap)
        
        return heapq.nsmallest(k, heap)[-1]
        
        
                