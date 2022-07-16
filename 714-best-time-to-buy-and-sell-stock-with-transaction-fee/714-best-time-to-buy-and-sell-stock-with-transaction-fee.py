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
        
        dp[0][0] = prices[0]
        

        for i in range(1, n):

            if dp[i-1][0] > prices[i]:
                dp[i][0] = prices[i]
                dp[i][1] = dp[i-1][1]
            elif dp[i-1][0] + fee < prices[i]:
                dp[i][1] = dp[i-1][1] + prices[i] - dp[i-1][0] - fee
                dp[i][0] = prices[i] - fee
            else:
                dp[i] = dp[i-1]

        return dp[-1][1]