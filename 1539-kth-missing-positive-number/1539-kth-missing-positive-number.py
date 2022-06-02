class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt, i, j = 0, 0, 1
        for _ in range(k):
            arr.append([])
        while cnt < k:
            if arr[i] != j:
                cnt += 1
                j += 1
            else:
                i += 1
                j += 1
        return j - 1
 