class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = fast = 0
        
        for i in range(len(nums)):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
                
        return slow