class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        base = 64
        for i in columnTitle:
            res = res*26 + ord(i) - base
            
        return res