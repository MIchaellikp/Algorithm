class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        a = len(s)
        next = ['' for i in range(a)]
        k = -1
        next[0] = k
        
        for i in range(1,a):
            while ( k > -1 and s[i] != s[k + 1]):
                k = next[k]
            if s[i] == s[k+1]:
                k += 1
                
            next[i] = k
        
        if next[-1] != -1 and a%(a-next[-1] -1) == 0:
            return True
        else:
            return False