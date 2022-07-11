class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = 0
        cur_s = 0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur_s += gas[i] - cost[i]
            
            if cur_s < 0:
                cur_s = 0
                start = i + 1
                
        if total < 0:
            return -1
        
        else:
            return start