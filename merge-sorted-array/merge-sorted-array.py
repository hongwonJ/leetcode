class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(m):
                nums1[i] = nums2[i]
                return
        if n == 0: return
        i, j, temp = 0, 0, []
        for k in range(m): temp.append(nums1[k])
        while i + j < m + n:
            if (j == n) or (i < m and temp[i] <= nums2[j]):
                nums1[i+j] = temp[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1
        return