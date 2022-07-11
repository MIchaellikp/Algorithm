class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        count = 0
        for i in range(len(s)):
            if count < len(g) and s[i] >= g[count]:
                count += 1
        return count