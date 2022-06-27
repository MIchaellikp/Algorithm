class Solution:
    def minPartitions(self, n: str) -> int:
        result = 0
        
        for i in n:
            if int(i) == 9:
                return 9
            if int(i) > result:
                result = int(i)
                
        return result