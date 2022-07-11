"""class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0 
        if len(nums) <= 1:
            return True
        i = 0
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1:
                return True
            i += 1
            
        return False"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        minIndex = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=minIndex:
                minIndex=i
        if minIndex==0:
            return True
        return False