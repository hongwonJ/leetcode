class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max = [nums[0]]
        n, m = len(nums), 1
        for i in range(n):
            if nums[i] not in max:
                sgn = False
                for j in range(m):
                    if nums[i] > max[j]:
                        max.append(nums[i])
                        max.sort(reverse=True)
                        m = len(max)
                        if len(max) > 3:
                            max.pop()
                            m = 3
                        sgn = True
                        break
                if not sgn:
                    max.append(nums[i])
                    m += 1
        return max[2] if len(max) >= 3 else max[0]


                
            
            
        