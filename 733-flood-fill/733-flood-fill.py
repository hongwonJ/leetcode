class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m, n = len(image), len(image[0])
        stack = []
        marked = [False]*(n*m)
        
        stack.append((sr,sc))
        sgn = image[sr][sc]
        image[sr][sc] = newColor

        
        while stack:
            r, c = stack.pop()
            marked[r*n + c] = True
            Adj = []
            if r-1 >= 0: Adj.append((r-1,c))
            if r+1 < m: Adj.append((r+1,c))
            if c-1 >= 0: Adj.append((r,c-1))
            if c+1 < n: Adj.append((r,c+1))
            
            for adjr, adjc in Adj:
                if not marked[adjr*n + adjc] and image[adjr][adjc] == sgn:     
                    image[adjr][adjc] = newColor
                    stack.append((adjr, adjc))
                marked[adjr*n + adjc] = True
                        
        return image
