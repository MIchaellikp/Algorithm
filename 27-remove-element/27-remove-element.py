class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = fast = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
                
        return slow