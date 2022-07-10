"""class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        
        cur=0
        dp0=cost[0]
        
        if len(cost) >= 2:
            dp1=cost[1]
        
        for i in range(2, len(cost)):
            cur=cost[i] + min(dp0,dp1)
            dp0=dp1
            dp1=cur
            
        return min(dp0,dp1)"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b=0,0
        for i in range(2,len(cost)+1):
            b,a = a,min(a+cost[i-1],b+cost[i-2])
        return a