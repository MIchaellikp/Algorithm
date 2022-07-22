class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        evenIndex = 0
        oddIndex = 1
        for i in range(len(nums)):
            if nums[i] % 2: 
                result[oddIndex] = nums[i]
                oddIndex += 2
            else: #偶数
                result[evenIndex] = nums[i]
                evenIndex += 2
        return result