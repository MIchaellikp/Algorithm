"""class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        def helper(start, n):
            if len(path) == len(nums):
                res.append(path[:])
                return
                
            for i in range(len(n)):
                path.append(n[i])
                helper(i+1, n[:i] + n[i+1:])
                path.pop()
                
                
        
        helper(0, nums)
        
        return res"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        backtrack([],nums,res,[])
        return res
    
def backtrack(curr,nums,res,usedIdx):
    if len(curr)==len(nums):
        res.append(curr[:])
        return
    
    for x in range(len(nums)):
        if not x in usedIdx:
            usedIdx.append(x)
            curr.append(nums[x])
            backtrack(curr,nums,res,usedIdx)
            curr.pop()
            usedIdx.pop()