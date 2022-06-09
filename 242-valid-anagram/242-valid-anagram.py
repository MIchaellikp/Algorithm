class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        
        for i in s:
            d[i] = d.get(i,0) + 1
            
        for j in t:
            if j not in d:
                return False
            else:
                d[j] -= 1
                if d[j] < 0:
                    return False
        if sum(d.values()) > 0:
            return False
        else:    
            return True