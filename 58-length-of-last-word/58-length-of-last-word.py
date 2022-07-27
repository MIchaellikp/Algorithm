class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        n = len(s) - 1
        while n > 0 and s[n] == ' ':
            n -= 1
        
        
        for i in range(n, -1, -1):
            if s[i] != ' ':
                res += 1
            else:
                return res
        return res