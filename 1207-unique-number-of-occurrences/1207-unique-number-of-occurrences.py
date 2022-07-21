class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = [0] * 2002
        
        for i in arr:
            c[i+1000] += 1
            
        f =[0] * 1002
        
        for i in c:
            if i > 0:
                if f[i] > 0:
                    return False
                else:
                    f[i] = 1
                    
        return True
                
        