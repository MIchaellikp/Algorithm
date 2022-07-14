class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in strs:
            z = i.count('0')
            o = i.count('1')
            
            for x in range(m,z-1,-1):
                for y in range(n, o - 1, -1):
                    dp[x][y] = max(dp[x][y], dp[x-z][y-o]+1)
        return dp[m][n]
                