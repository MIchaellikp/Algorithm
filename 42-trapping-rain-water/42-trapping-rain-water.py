class Solution:
    def trap(self, height: List[int]) -> int:
        """l = 0
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
                
        return res"""
#         lh, rh = [0] * len(height), [0] * len(height) 
        
#         lh[0] = height[0]
        
#         for i in range(1, len(height)):
#             lh[i] = max(height[i], lh[i-1])
            
#         rh[-1] = height[-1]
        
#         for i in range(len(height)-2, -1, -1):
#             rh[i] = max(rh[i+1], height[i])
        
#         ans = 0
#         for i in range(len(height)):
#             ans += min(lh[i], rh[i]) - height[i]
            
#         return ans
        stack = [0]
        ans = 0
        for i in range(1, len(height)):
            if stack and height[i] > height[stack[-1]]:
                while stack and height[i] > height[stack[-1]]:
                    stand = height[stack.pop()]
                    if stack:
                        l = height[stack[-1]]
                        r = height[i]
                        h = min(l,r) - stand
                        w = i - stack[-1] -1
                        ans += h*w
            elif height[i] == height[stack[-1]]:
                stack.pop()
            
            stack.append(i)
            
        return ans

