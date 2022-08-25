class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        start, cnt = 0, 0
        
        while cnt < n:
            tmp = nums[start]
            imoved = (start + k) % n
            while True: 
                nums[imoved], tmp = tmp, nums[imoved]
                cnt += 1
                if imoved == start: break
                imoved = (imoved + k) % n
            start += 1
            
        return nums
        
        
'''
        start, count = 0, 0
        
        while count < n:
            curr, saved = start, nums[start]
            while True:
                next_idx = (curr+k) % n
                nums[next_idx], saved = saved, nums[next_idx]
                curr = next_idx
                count += 1
                
                if start == curr:
                    break
            start += 1
'''