class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = len(cardPoints) - k
        mins = float('inf')
        curr = j = 0
        
        for i,v in enumerate(cardPoints):
            curr += v
            if i - j + 1 > s:
                curr -= cardPoints[j]
                j += 1
                
            if i - j + 1 == s:
                mins = min(curr, mins)
                
        return sum(cardPoints) - mins
                