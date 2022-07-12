class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 0: return intervals
        
        res = []
        
        intervals.sort(key = lambda x: x[0])
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            last = res[-1]
            if last[1] >= intervals[i][0]:
                res[-1] = [last[0], max(last[1], intervals[i][1])]
            else:
                res.append(intervals[i])
                
        return res