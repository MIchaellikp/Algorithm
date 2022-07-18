class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        count = 1
        res = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1
              
            res = max(res, count)
            
        return res