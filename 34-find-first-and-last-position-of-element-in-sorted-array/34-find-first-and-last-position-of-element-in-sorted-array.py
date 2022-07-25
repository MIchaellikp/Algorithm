class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        def rb(n,r):
            l, r = 0, len(n) - 1
            rib = -2
            while l <= r:
                m = l + (r - l) //2
                if n[m] > target:
                    r = m - 1
                else:
                    l = m + 1
                    rib = l
            return rib
        
        def lf(n, r):
            l, r = 0, len(n) - 1
            leb = -2
            while l <= r:
                m  = l + (r - l) //2
                if n[m] < target:
                    l = m + 1
                else:
                    r = m - 1
                    leb = r
            return leb
        
        
        leb = lf(nums,target)
        rib = rb(nums, target)
        
        if leb == -2 or rib == -2:
            return [-1,-1]
        if rib - leb > 1:
            return [leb + 1, rib - 1]
        return [-1,-1]