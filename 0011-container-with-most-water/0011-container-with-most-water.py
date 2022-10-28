from collections import defaultdict


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        max_area = 0
        while i < j:
            area = (j-i)*min(height[i],height[j])
            max_area = max(area, max_area)
            if height[i] > height[j]: j -= 1
            else: i += 1
                
        return max_area
