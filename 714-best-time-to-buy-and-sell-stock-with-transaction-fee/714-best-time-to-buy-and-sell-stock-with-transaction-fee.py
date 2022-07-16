class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res = 0
        pp = prices[0]
        
        for i in range(1, len(prices)):
            if pp > prices[i]:
                pp = prices[i]
            elif prices[i] > pp + fee:
                res += prices[i] - pp - fee
                pp = prices[i] - fee
            
        return res