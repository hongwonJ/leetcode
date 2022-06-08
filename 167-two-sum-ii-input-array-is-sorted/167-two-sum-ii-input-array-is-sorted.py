class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers) - 1):
            a, b = i + 1, len(numbers) - 1
            ntarget = target - numbers[i]
            while a <= b:
                c = (a + b)//2                
                if numbers[c] == ntarget: return [i + 1, c + 1]
                elif numbers[c] < ntarget: a = c + 1
                else: b = c - 1