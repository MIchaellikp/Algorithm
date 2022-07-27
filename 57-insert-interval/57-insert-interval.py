class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #1 insert sort then merge
        
        intervals.append(newInterval)
        
        intervals.sort(key = lambda x: x[0])
        
        res = []
        res.append(intervals[0])
        for i in range(len(intervals)):
            last = res[-1]
            if intervals[i][0] <= last[1]:
                res[-1][1] = max(intervals[i][1], last[1])
            else:
                res.append(intervals[i])
                
        return res