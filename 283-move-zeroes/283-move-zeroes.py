class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                slow += 1
                
            else:
                nums[i-slow],nums[i] = nums[i], nums[i-slow]