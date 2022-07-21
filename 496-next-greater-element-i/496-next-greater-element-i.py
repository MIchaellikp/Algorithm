class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = [nums2[0]]
        
        for i in range(1,len(nums2)):
            if stack and nums2[i] > stack[-1]:
                
                while stack and nums2[i] > stack[-1]:
                    s = stack.pop()
                    if s in nums1:
                        res[nums1.index(s)] = nums2[i]
 
            stack.append(nums2[i])
        
        return res