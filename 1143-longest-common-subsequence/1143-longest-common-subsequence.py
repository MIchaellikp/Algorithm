class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        dp = [[0] * (n) for _ in range( m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j] = (dp[i-1][j-1] if i > 0 and j > 0 else 0) + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 

                    
        return dp[-1][-1]
        