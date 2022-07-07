"""class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        def helper(start):
            if len(path) >= 2:
                res.append(path[:])
            
            if len(path) > len(nums):
                return
            
            usage_list = set()
            
            for i in range(start, len(nums)):
                if (nums[i] in usage_list) or ( path and nums[i] < path[-1]):
                    continue
                usage_list.add(nums[i])
                path.append(nums[i])
                helper(i + 1)
                path.pop()
                
                
        helper(0)
        return res"""

class Solution:
    def findSubsequences(self, n) :
        out={}
        for i in n :
            t={(i,)}

            for v in out : 
                t.add(v)

                if v[-1]<=i :
                    t.add(v+(i,)) 
            out = t

        return [i for i in out if len(i)>1]
