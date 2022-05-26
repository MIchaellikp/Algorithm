class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], - x[1]))
        tails = [0] * len(envelopes)
        size = 0
        
        
        for i in range(len(envelopes)):
            l, r = 0, size
            while l != r:
                m = (l + r) // 2
                if tails[m] < envelopes[i][1]:
                    l = m + 1
                else:
                    r = m
            tails[l] = envelopes[i][1]
            size = max(size, l + 1)
                
        return size
                