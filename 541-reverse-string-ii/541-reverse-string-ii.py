"""class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #1.0
        a = list(s)
        n = len(s)
        for i in range(0, n , k * 2):
            l = i
            r = min(n - 1,i + k -1)
            while l < r:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1
                
                
        return "".join(a)"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Two pointers. Another is inside the loop.
        p = 0
        while p < len(s):
            p2 = p + k
            # Written in this could be more pythonic.
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s