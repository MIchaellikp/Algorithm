class Solution:
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
                
                
        return "".join(a)