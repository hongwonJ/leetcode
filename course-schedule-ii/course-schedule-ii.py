class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        graph = {i:[] for i in range(numCourses)}
        indeg = {i: 0 for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indeg[crs] += 1
        
        able = collections.deque([i for i in range(numCourses) if indeg[i] == 0])
        while able:
            crs = able.popleft()
            ans.append(crs)
            for nxt in graph[crs]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    able.append(nxt)
        
        return ans if len(ans) == numCourses else []

