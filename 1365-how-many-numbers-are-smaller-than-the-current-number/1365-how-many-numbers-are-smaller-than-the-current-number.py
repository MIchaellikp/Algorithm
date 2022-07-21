class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = nums[:]
        res.sort()
        
        d = {}
        
        for i,v in enumerate(res):
            if v not in d.keys():
                d[v] = i
        
        for i, v in enumerate(nums):
            res[i] = d[v]
            
        return res