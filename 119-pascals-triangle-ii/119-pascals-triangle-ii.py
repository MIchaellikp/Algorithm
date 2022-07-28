class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [1] * 2
        p = [1]
        if rowIndex == 0:
            return p
        if rowIndex == 1:
            return cur
        
        
        
        for i in range(2, rowIndex + 1):
            p = cur
            cur = [1] * (i+1)
            
            for j in range(1, i):
                cur[j] = p[j-1] + p[j]
                
            
        return cur