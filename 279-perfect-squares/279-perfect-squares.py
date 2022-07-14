class Solution:
    """def numSquares(self, n: int) -> int:
        '''版本二， 先遍历物品, 再遍历背包'''
        # 初始化
        nums = [i**2 for i in range(1, n + 1) if i**2 <= n]
        dp = [n+1]*(n + 1)
        dp[0] = 0
        # 遍历物品
        for num in nums:
            # 遍历背包
            for j in range(num, n + 1):
                dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]"""
    def numSquares(self, n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        d, q, nq = 1, {n}, set()
        while q:
            for node in q:
                for square in squares:
                    if node == square: return d
                    if node < square: break
                    nq.add(node-square)
            q, nq, d = nq, set(), d+1