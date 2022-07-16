class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0]*4 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], max(dp[i-1][1], dp[i-1][3]) - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][3]) # previous sold stock or before the cooldown sold stock but keep track the status like 0,3,5
            dp[i][2] = dp[i-1][0] + prices[i] #sold sotck
            dp[i][3] = dp[i-1][2] # cooldown inital
            
            
        return max(dp[n-1][3], dp[n-1][1], dp[n-1][2])