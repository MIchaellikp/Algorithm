"""class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2:
            return False
        else:
            temp =sum(nums)//2
        
        
        dp = [0] * (temp+1)
        
        for i in range(len(nums)):
            for j in range(temp, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[temp] == temp""" 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        @lru_cache(maxsize=None)
        def recursive(n: int, current_sum: int):
            if current_sum == 0:
                return True
            elif current_sum < 0 or n == len(nums) - 1:
                return False
            
            return recursive(n + 1, current_sum - nums[n + 1]) or recursive(n + 1, current_sum)
        
        return recursive(0, target)