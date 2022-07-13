class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        
        
        
        d = [0] * (2)
        
        d[0] = 0
        d[1] = 1
        
        for i in range(2, n+1):
            temp = d[0] + d[1]
            d[0] = d[1]
            d[1] = temp
            
        return d[-1]