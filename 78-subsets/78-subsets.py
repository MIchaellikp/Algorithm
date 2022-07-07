class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        
        def helper(start):
            res.append(path[:])
            
            if start == len(nums):
                return 
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                helper(i+1)
                path.pop()
                
            
        helper(0)
        
        return res