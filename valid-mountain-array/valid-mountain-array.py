class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        alt, down = False, False
        if len(arr) < 3 or (arr[0] > arr[1]): return False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]: return False
            elif arr[i] > arr[i+1]:
                alt = True
                down = True
            else:
                down = False
                if alt == True and down == False: return False
        return True if alt == True and down == True else False
                
                