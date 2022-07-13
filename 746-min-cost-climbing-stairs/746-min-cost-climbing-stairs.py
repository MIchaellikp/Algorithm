class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a , b = 0 ,0 
        
        for i in range(2, len(cost) + 1):
            b, a = a, min( a + cost[i-1], b + cost[i-2])
            
        return a