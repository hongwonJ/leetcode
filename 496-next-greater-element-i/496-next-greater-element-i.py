class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n1, n2 = len(nums1), len(nums2)
        for n in nums1:
            i = 0
            while i < n2 and nums2[i] != n: i += 1
            j = i
            while j < n2:
                if nums2[i] < nums2[j]:
                    ans.append(nums2[j])
                    break
                j += 1
            if j == n2: ans.append(-1)
                
        return ans
            
            