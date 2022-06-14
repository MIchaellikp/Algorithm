class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #slide window
        """
        start = 0
        result = 0 
        temp = 0
        
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
                temp += nums[i]
            else:
                if hashmap[nums[i]] < start:
                    hashmap[nums[i]] = i
                    temp += nums[i]
                else:
                    result = max(result, temp)
                    temp -= sum(nums[start: hashmap[nums[i]]])
                    start = hashmap[nums[i]] + 1
                    hashmap[nums[i]] = i
                    
        return max(result, temp) 
        """
        seen = set()
        cur_max = 0
        l = 0
        result = 0
        
        for i in nums:
            while i in seen:
                cur_max -= nums[l]
                seen.remove(nums[l]) 
                l += 1
            cur_max += i
            seen.add(i)
            result = max(cur_max, result)
            
        return result
                
        