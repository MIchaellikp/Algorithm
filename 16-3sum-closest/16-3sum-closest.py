"""class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):

            # update: ignore the duplicate numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r] + nums[i]
                if curSum == target:
                    return target
                if abs(curSum-target) < abs(result-target):
                    result = curSum
                if curSum < target:
                    l += 1
                else:
                    r -= 1
        return result"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 100000
        n = len(nums)
        for i in range(n-2):
            x = nums[i] + nums[-2] + nums[-1]
            if x < target:
                if abs(x-target) < abs(ans-target):
                    ans = x
                continue
            y = nums[i] + nums[i+1] + nums[i+2]
            if y > target:
                if abs(y-target) < abs(ans-target):
                    ans = y
                break
            a=nums[i]
            k = i+1
            e = n-1
            while k < e:
                s = nums[k] + nums[e]
                if s==target-a:
                    return target
                if abs(s+a-target)<abs(ans-target):
                    ans=s+a
                if s < target-a:
                    k += 1
                else:
                    e -= 1
        return ans