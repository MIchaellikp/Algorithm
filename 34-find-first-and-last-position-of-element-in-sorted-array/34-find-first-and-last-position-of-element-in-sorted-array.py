class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def rightsearch (nums:List[int], target:int):
            l, r = 0, len(nums) - 1
            ri = -2
            while (l <= r):
                m = (l+r)//2
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
                    ri = l
                    
            return ri
        
        def leftsearch (nums:List[int], target:int):
            l, r = 0, len(nums) - 1
            li = -2
            while (l <= r):
                m = (l+r)//2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
                    li = r
                    
            return li
                
        a = rightsearch (nums, target)
        b = leftsearch (nums, target)
        
        
        if a == -2 or b == -2: return [-1, -1]

        if a - b > 1:
            return [b+1, a-1]
        
        return [-1, -1]