from collections import defaultdict


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = []
        
        h_max = max(height)
        height_dict = defaultdict(list)
        for ih, h in enumerate(height):
            height_dict[h].append(ih)
        min_, max_ = 0, len(height)-1
        
        min_list = []
        max_list = []
        
        i_min, i_max = min_, max_
        for h in range(0, h_max + 1):
            if height[i_min] >= h: min_list.append(i_min)
            else:
                while height[i_min] < h:
                    i_min += 1
                min_list.append(i_min)
            if height[i_max] >= h: max_list.append(i_max)
            else:
                while height[i_max] < h:
                    i_max -= 1
                max_list.append(i_max)
                    
        
        for h in range(0, h_max + 1):
            if h in height_dict:
                min_ih, max_ih = height_dict[h][0], height_dict[h][-1]
                area.append(max(h*(max_list[h]-min_ih), h*(max_ih - min_list[h])))
  
        return max(area)
