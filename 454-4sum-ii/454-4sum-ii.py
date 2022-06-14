class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #hashmap 
        
        d = {}
        
        for i in nums1:
            for j in nums2:
                d[-(i+j)] = d.get(-(i+j),0) + 1
                
        result = 0
        for i in nums3:
            for j in nums4:
                if (i + j) in d:
                    result += d[i+j]
                    
        return result
                    