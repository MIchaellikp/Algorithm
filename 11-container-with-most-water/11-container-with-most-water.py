class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        l, r = 0, len(height) - 1
        lm = 0
        rm = 0
        
        while l < r:
            if height[l] > height[r]:
                res = max(height[r]*(r-l), res)
                r -= 1
            else:
                res = max(height[l]*(r-l), res)
                l += 1
                
        return res