class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rs = sum(nums)
        
        ls = 0
        
        for i in range(len(nums)):
            rs -= nums[i]
            if i > 0:
                ls += nums[i-1]
                
            if rs == ls:
                return i
            
        return -1