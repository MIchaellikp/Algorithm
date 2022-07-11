class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = [nums[0]]
        res = nums[0]
        
        for i in range(1, len(nums)):
            if temp[i-1] >= 0 :
                temp.append(temp[i-1] + nums[i])
            else:
                temp.append(nums[i])
                
            res = max(temp[i], res)
            
        return res