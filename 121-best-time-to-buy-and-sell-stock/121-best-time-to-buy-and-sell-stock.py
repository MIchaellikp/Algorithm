"""class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if len == 0:
            return 0
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        return dp[-1][1]"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        
        max_price=0
        
        curr_price=0
        
        min_ele=prices[0]
        
        for i in range(1,n):
            curr_price=prices[i]-min_ele
            
            if max_price<curr_price:
                max_price=curr_price
                
            if prices[i]<min_ele:
                min_ele=prices[i]
                
        return max_price