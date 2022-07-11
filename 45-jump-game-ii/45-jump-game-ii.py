class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        cover = 0
        if len(nums) <=1 :
            return 0
        curp = 0
        for i in range(len(nums)):
            cover = max(i+nums[i], cover)
            if i == curp:
                res += 1
                curp = cover
                if cover >= len(nums) - 1:
                    break
                    
        return res