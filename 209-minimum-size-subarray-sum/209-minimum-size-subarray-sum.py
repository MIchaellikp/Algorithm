class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        temp = 0
        result = len(nums) + 1
        for i in range(len(nums)):
            temp += nums[i]
            
            while temp >= target:
                result = min(result, i - s + 1)
                temp -= nums[s]
                s += 1
                
        if result == len(nums) + 1:
            return 0
        else:
            return result
