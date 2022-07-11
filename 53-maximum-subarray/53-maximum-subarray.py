class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = 0
        res = nums[0]
        
        for i in range(len(nums)):
            count += nums[i]
            if count >= res:
                res = count
            if count <= 0:
                count = 0
            
        return res