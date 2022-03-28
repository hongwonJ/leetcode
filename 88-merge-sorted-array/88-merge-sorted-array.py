class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if(m+n > 0):
            if (n == 0) or (m > 0 and nums1[m-1] >= nums2[n-1]):
                nums1[m+n-1] = nums1[m-1]
                self.merge(nums1, m-1, nums2, n)    
            else:
                nums1[m+n-1] = nums2[n-1]
                self.merge(nums1, m, nums2, n-1)    
            