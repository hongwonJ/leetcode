class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in range(len(arr)-1, -1, -1):
            tmp, arr[i] = arr[i], max
            if max == -1 or tmp > max: max = tmp
        return arr
            
                
        
            