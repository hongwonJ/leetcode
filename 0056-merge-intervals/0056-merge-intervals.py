class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        startset = dict()
        min_, max_ = float('inf'), float('-inf')
        for interval in intervals:
            if interval[0] not in startset or interval[1] > startset[interval[0]]:
                startset[interval[0]] = interval[1]
                if interval[0] < min_: min_ = interval[0]
                if interval[1] > max_: max_ = interval[1]    

        n = min_
        ans = []
        while n <= max_: 
            if n in startset:
                k, endpoint = n+1, startset[n]
                while k < endpoint + 1:
                    if k in startset and startset[k] > endpoint:
                        endpoint = startset[k]
                        overlap = True
                    k += 1
                ans.append([n, endpoint])
                n = endpoint + 1
            else: n += 1

        return ans
                
                        
            
            
            
            
            
            
                