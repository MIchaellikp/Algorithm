class Solution:
    def mySqrt(self, x: int) -> int:
        l ,r = 1, x
        if (x==0):
            return 0
        
        while (l <= r):
            m = (l+r) // 2
            if m*m > x:
                r = m - 1 
            else:
                if (m+1)*(m+1) > x:
                    return m
                else:
                    l = m + 1
                    
        