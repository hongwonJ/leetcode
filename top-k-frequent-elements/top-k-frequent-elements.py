import collections as col
import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        cntDict = col.Counter(nums)
        return hq.nlargest(k, cntDict, cntDict.get)
        