class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        n = 0
        o = x
        while o > 0:
            n = o % 10 + n*10
            o = o//10
            
        return n == x