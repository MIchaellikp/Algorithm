class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (hi-lo)//2+lo
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lo = mid+1
            else:
                hi = mid
        return lo if nums[lo]==target else -1
            