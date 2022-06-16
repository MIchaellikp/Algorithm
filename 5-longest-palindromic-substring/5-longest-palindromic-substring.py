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
                            
        return result
    
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
        return ans"""
    

    def longestPalindrome(self, s: str) -> str:
        # solution 5
        # optimze solution 3 by speeding with existed len
        # AC, 97.61% speed, 59.88% memory
        n = len(s)
        def dfs(beg, end):
            while 0<=beg and end < n and s[beg] == s[end]:
                beg -= 1
                end += 1
            return (beg+1, end)
        res, m = (0, 1), 1
        for pos in range(n-1):
            if m // 2 + pos >= n:
                break
            div, rem = divmod(m, 2)

            if s[pos-div+(m-1)%2:pos] != s[pos+1:pos+div+rem][::-1]:
                s1 = (0, 0)
            else:
                s1 = dfs(pos-div-rem, pos+div+rem)
            if s[pos-div+1:pos+1] != s[pos+1:pos+div+1][::-1]:
                s2 = (0, 0)
            else:
                s2 = dfs(pos-div, pos+div+1)

            if s1[1] - s1[0] > m:
                res, m = s1, s1[1] - s1[0]
            if s2[1] - s2[0] > m:
                res, m  = s2, s2[1] - s2[0]
        return s[res[0]:res[1]]
        