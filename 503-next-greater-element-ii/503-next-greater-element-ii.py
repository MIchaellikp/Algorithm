class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        
        stack = [0]
        
        for i in range(1, len(nums)):
            if stack and nums[i] > nums[stack[-1]]:
                while stack and nums[i] > nums[stack[-1]]:
                    s = stack.pop()
                    res[s] = nums[i]
                    
            stack.append(i)
            
        for i in range(len(nums)):
            if stack and nums[i] > nums[stack[-1]]:
                while stack and nums[i] > nums[stack[-1]]:
                    s = stack.pop()
                    res[s] = nums[i]
                    
            stack.append(i)
            
        return res