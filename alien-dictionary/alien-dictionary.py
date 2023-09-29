class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {c:[] for word in words for c in word}
        indeg = {c : 0 for word in words for c in word}
        for word1, word2 in zip(words[:-1], words[1:]):
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].append(c2)
                        indeg[c2] += 1
                    break
            else:
                if len(word2) < len(word1):
                    return ""

        n = len(graph.keys())
        dict_order = []
        curr = collections.deque([char for char, ind in indeg.items() if ind == 0])
        while curr:
            char = curr.popleft()
            dict_order.append(char)
            for nxt in graph[char]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    curr.append(nxt)

        return ''.join(dict_order) if len(dict_order) == n else ""
            

        

