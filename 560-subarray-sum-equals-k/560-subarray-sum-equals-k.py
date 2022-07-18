class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        d = {0:1}
        prefix = 0
        
        for i in nums:
            prefix += i
            
            if prefix - k in d:
                ans += d[prefix-k]
                
            d[prefix] = d.get(prefix,0) + 1
            
            
        return ans
            
            