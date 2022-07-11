class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        ans = []
        cnt = dict()
        for n in nums2:
            if n not in cnt: cnt[n] = 1
            else: cnt[n] += 1
        
        for n in nums1:
            if n in cnt and cnt[n] > 0:
                ans.append(n)
                cnt[n] -= 1
        
        return ans
                
            
        