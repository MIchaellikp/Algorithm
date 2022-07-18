class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [0] * (n+1)
        result = 0
        for i in range(1,m+1):
            for j in range(n, 0, -1 ):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                else:
                    dp[j] = 0
                result = max(dp[j], result)
        return result