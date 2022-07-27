class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        l, r = 0, len(height) - 1
        lm = 0
        rm = 0
        
        while l < r:
            lm = max(lm,height[l])
            rm = max(rm,height[r])
            if lm > rm:
                res = max(rm*(r-l), res)
                r -= 1
            else:
                res = max(lm*(r-l), res)
                l += 1
                
        return res