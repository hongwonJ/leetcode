class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        matList = []
        
        for i in range(n):
            for j in range(n):
                self.insertHeap(matList, matrix[i][j])
                
        for _ in range(k):
            matList[0], matList[-1] = matList[-1], matList[0]
            x = matList.pop()
            self.min_down(matList)
        
        return x
        
        
    def min_down(self, heap):
        i, n = 0, len(heap)
        while 2*i+1 < n:
            l, r = 2*i + 1, 2*i + 2
            if r == n or heap[l] <= heap[r]: min_i = l
            else: min_i = r
            if heap[i] < heap[min_i]: break
            heap[i], heap[min_i] = heap[min_i], heap[i]
            i = min_i
    
    def min_up(self, heap):
        i = len(heap) - 1
        while (i-1)//2 >= 0:
            up_i = (i-1)//2
            if heap[(i-1)//2] < heap[i]: break
            heap[i], heap[up_i] = heap[up_i], heap[i]
            i = up_i
        
    def insertHeap(self, heap, n):
        heap.append(n)
        self.min_up(heap)
        
    