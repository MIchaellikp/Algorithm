class Solution:
    """
    def longestPalindrome(self, s: str) -> str:
        dp = [ [0]*len(s) for _ in range(len(s))]
        result = s[0]
        for i in range(len(s)):
            dp[i][i] = True
            
            
        for i in range( len(s) -1, -1, -1):
            for j in range( i + 1, len(s)):
                #print(dp)
                if s[i] == s[j]:
                    if j - i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        if len(result) < j - i:
                            result = s[i:j+1]
                            
        return result"""
    
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s)) ]
        for i in range(len(s)):
            dp[i][i]=True
        ans=s[0]
        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j]=True
                    if j-i+1>len(ans):
                        ans=s[i:j+1]
        return ans
        