class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        if m < n:
            return False
        
        a = 0
        b = 0
        
        while a < n and b < m:
            if s[a] == t[b]:
                a += 1
                b += 1
            else:
                b += 1
                
        if a == n and b <= m:
            return True
        else:
            return False