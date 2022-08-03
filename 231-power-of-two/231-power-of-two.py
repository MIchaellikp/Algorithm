class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        
        if n == 0:
            return False

        
        while n> 1:
            if n%2:
                return False
            n = n//2
            
        if n == 1:
            return True
        else:
            return False