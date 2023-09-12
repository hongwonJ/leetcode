class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        def build(edges, restricted):
            graph = collections.defaultdict(list)
            for n1, n2 in edges:
                if n1 not in restricted and n2 not in restricted:
                    graph[n1].append(n2)
                    graph[n2].append(n1)
            return graph
        graph = build(edges, restricted)
        
        seen = set()
        count = [0]
        def dfs(node):
            seen.add(node)
            count[0] += 1
            for adj in graph[node]:
                if adj not in seen: 
                    dfs(adj)
        dfs(0)
        return count[0]
            








