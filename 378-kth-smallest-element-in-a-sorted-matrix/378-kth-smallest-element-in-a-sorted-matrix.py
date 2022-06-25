import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                heap.append(matrix[i][j])
            
        heapq.heapify(heap)
        
        return heapq.nsmallest(k, heap)[-1]
        
        
                