class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        
        
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[slow] = nums[i+1]
                slow += 1
                
        return slow