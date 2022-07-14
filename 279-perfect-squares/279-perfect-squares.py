class Solution:
    def numSquares(self, n: int) -> int:
        '''版本二， 先遍历物品, 再遍历背包'''
        # 初始化
        nums = [i**2 for i in range(1, n + 1) if i**2 <= n]
        dp = [10**4]*(n + 1)
        dp[0] = 0
        # 遍历物品
        for num in nums:
            # 遍历背包
            for j in range(num, n + 1):
                dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]