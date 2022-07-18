class Solution:
    """def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i-1] >= 0:
                nums[i] += nums[i-1]
            res = max(res, nums[i])
            
        return res"""
    
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) #状态转移公式
            result = max(result, dp[i]) #result 保存dp[i]的最大值
        return result