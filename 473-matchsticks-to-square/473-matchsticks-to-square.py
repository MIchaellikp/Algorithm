class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        
        if len(matchsticks) < 4:
            return False
        
        s = sum(matchsticks)
        
        if s % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True)
        target = s//4
        
        path = [0] * 4
        
        
        def helper(i):
            
            if i == len(matchsticks):
                return path[0] == path[1] == path[2] == path[3] == target
            
            for j in range(4):
                if path[j] + matchsticks[i] <= target:
                    path[j] += matchsticks[i]
                    if helper(i + 1):
                        return True
                    path[j] -= matchsticks[i]
            return False
        
        return helper(0)
                
                