class Solution:
    def lengthOfLIS(self, nums):
        tails = [1] * len(nums)
        size = 0
        for i in range(1,len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tails[i] = max(tails[i], tails[j] + 1)
        return max(tails)