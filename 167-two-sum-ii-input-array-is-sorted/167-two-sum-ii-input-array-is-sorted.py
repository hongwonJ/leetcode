class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        for i in range(n-1):
            sum = numbers[i]
            a, b = i + 1, n - 1
            while a <= b:
                c = (a+b)//2
                if sum + numbers[c] == target: return [i+1, c+1]
                elif sum + numbers[c] < target: a = c+1
                else: b = c-1
            
            