class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(2)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            tmp=dp[0]+dp[1]
            dp[0]=dp[1]
            dp[1]=tmp
        return dp[1]