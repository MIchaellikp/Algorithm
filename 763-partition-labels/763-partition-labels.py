class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = [0] * 26
        
        for i in range(len(s)):
            d[ord(s[i]) - ord('a')] = i
        l = 0
        res = []
        r = 0
        for i in range(len(s)):
            r = max(d[ord(s[i]) - ord('a')], r)
            if i == r:
                res.append(r - l + 1)
                l = i + 1
                
        return res
                
        