class Solution:
    def reverse(self, x: int) -> int:
        c = 1
        if x < 0: 
            c = -1 
            x = -x
        res = 0
        while x > 0:
            a = x % 10
            res = res*10 + a
            x = x//10
        return res * c if (res < 2 **31) else 0