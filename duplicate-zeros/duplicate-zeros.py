class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n, cntArr, cnt = len(arr), [], 0
        for i in range(n):
            cntArr.append(cnt)
            if arr[i] == 0:
                cntArr[i] = -cnt - 1
                cnt += 1
        for i in range(n - 1, -1, -1):
            if cntArr[i] >= 0:
                if i + cntArr[i] < n: arr[i + cntArr[i]] = arr[i]
            else:
                for j in range(2):
                    if (i - (cntArr[i] + 1) + j) < n: arr[i - (cntArr[i] + 1) + j] = 0
                
                
            
            