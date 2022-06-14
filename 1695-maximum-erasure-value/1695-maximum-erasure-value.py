class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #slide window
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
        