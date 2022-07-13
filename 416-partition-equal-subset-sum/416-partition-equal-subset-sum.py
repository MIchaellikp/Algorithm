class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2:
            return False
        else:
            temp =sum(nums)//2
        
        
        dp = [0] * (temp+1)
        
        for i in range(len(nums)):
            for j in range(temp, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[temp] == temp 