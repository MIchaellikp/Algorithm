class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in wordDict:
                if i >= len(j):
                    dp[i] = dp[i] or dp[i-len(j)] and j == s[i-len(j):i]
                    
        return dp[len(s)]