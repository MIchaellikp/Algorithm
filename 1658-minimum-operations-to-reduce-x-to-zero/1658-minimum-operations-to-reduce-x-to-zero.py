class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        a = sum(nums)
        
        if a < x:
            return -1
        if a == x:
            return len(nums)
        
        a = a - x
        l = 0
        cur = 0
        result = 0
        for i, v in enumerate(nums):
            cur += v
            while cur > a:
                cur -= nums[l]
                l += 1
            if cur == a:
                result = max(i - l + 1, result)
                
        return len(nums) - result if result > 0 else -1
        