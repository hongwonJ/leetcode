import heapq as hq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        flist, blist = [], []
        for interval in intervals:
            flist.append(interval[0])
            blist.append(interval[1])
        flist.append(float(inf))
        blist.append(float(inf))
        
        hq.heapify(flist)
        hq.heapify(blist)
        
        f, b = hq.heappop(flist), hq.heappop(blist)
        
        max_cnt, cnt = 1, 0
        
        while flist:
            if f == float(inf): return max_cnt
            if f < b:
                cnt += 1
                if cnt > max_cnt: max_cnt = cnt
                f = hq.heappop(flist)
            else:
                cnt -= 1
                b = hq.heappop(blist)
            
        return max_cnt
            
            
        
        
        