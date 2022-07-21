class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0,0)
        heights.append(0)
        stack = [0]
        
        ans = 0
        
        for i in range(1, len(heights)):
            if stack and heights[i] < heights[stack[-1]]:
                while stack and heights[i] < heights[stack[-1]]:
                    stand = stack.pop()
                    if stack:
                        h = heights[stand]
                        l = stack[-1]
                        w = i - l - 1
                        ans = max(ans, h*w)
                    
            stack.append(i)
            
        return ans 