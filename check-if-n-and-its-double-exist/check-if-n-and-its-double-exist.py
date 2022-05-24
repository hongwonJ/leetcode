class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in arr[i+1:]:
                if arr[i]*2 == j or arr[i]==j*2: return True
        return False
        