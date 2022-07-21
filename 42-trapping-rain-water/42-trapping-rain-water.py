class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lm, rm = 0,0 
        res = 0
        while l < r:
            if height[l] < height[r]:
                if lm < height[l]:
                    lm = height[l]
                else:
                    res += lm - height[l]
                l += 1
            else:
                if rm < height[r]:
                    rm = height[r]
                else:
                    res += rm - height[r]
                    
                r -= 1
                
        return res