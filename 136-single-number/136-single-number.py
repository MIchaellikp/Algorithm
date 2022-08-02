class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        
        return min(c.keys(), key = c.get)