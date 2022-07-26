class Solution:
    def minCut(self, s: str) -> int:
        dp = [ [0] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = 1
                        
                        
        dp1=[2000]*len(s)
        dp1[0]=0

        for i in range(1,len(s)):
            if dp[0][i]:
                dp1[i]=0
                continue
            for j in range(0,i):
                if dp[j+1][i]==True:
                    dp1[i]=min(dp1[i], dp1[j]+1)

        return dp1[-1]