class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        
        for i in range(len(s)-9):
            c = s[i:i+10]
            if c in seen:
                res.add(c)
            else:
                seen.add(c)
                
        return list(res)
            