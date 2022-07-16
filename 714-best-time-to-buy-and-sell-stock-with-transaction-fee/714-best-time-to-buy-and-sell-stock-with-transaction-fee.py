class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """res = 0
        pp = prices[0]
        
        for i in range(1, len(prices)):
            if pp > prices[i]:
                pp = prices[i]
            elif prices[i] > pp + fee:
                res += prices[i] - pp - fee
                pp = prices[i] - fee
            
        return res"""

        
        n = len(prices)
        dp = [[0,0] for i in range(n)]
        
        dp[0][0] = -prices[0]
        

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)

        return dp[-1][1]