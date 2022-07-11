class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        c, p, res = 0,0,1
        
        for i in range(len(nums) - 1):
            c = nums[i+1] - nums[i]
            if c*p <= 0 and c != 0:
                res += 1
                p = c
                
        return res