class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]
        rank = [1] * n
        count = n
        
        def find(x):
            if root[x] == x: return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y, count):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] == rank[rootY]:
                    root[rootY] = rootX
                    rank[rootX] += 1
                elif rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                else:
                    root[rootX] = rootY
                count -= 1
            return count
        
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1: count = union(i,j, count)
        
        return count